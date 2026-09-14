#!/usr/bin/env python3
"""Synchronize homepage publications and news from a DBLP person record."""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Iterable


DEFAULT_DBLP_PID = "257/8328-1"
DEFAULT_SOURCE = f"https://dblp.org/pid/{DEFAULT_DBLP_PID}.xml"
DEFAULT_BIB_SOURCE = f"https://dblp.org/pid/{DEFAULT_DBLP_PID}.bib"
GENERATED_BY = "dblp_sync"
USER_AGENT = "Anson-He-Academic-Homepage/1.0 (publication metadata sync)"
MONTHS = {
    "jan": 1,
    "feb": 2,
    "mar": 3,
    "apr": 4,
    "may": 5,
    "jun": 6,
    "jul": 7,
    "aug": 8,
    "sep": 9,
    "oct": 10,
    "nov": 11,
    "dec": 12,
}


@dataclass(frozen=True)
class Publication:
    key: str
    entry_type: str
    publtype: str
    title: str
    authors: tuple[tuple[str, str], ...]
    year: int
    month: str
    venue: str
    volume: str
    number: str
    pages: str
    paper_url: str


def fetch_source(source: str, accept: str = "application/xml") -> bytes:
    if not source.startswith(("http://", "https://")):
        return Path(source).read_bytes()

    request = urllib.request.Request(
        source,
        headers={"Accept": accept, "User-Agent": USER_AGENT},
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return response.read()
        except urllib.error.HTTPError as error:
            if error.code != 429 or attempt == 2:
                raise
            retry_after = min(int(error.headers.get("Retry-After", "5")), 60)
            time.sleep(retry_after)
        except urllib.error.URLError:
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)
    raise RuntimeError("DBLP request failed after retries")


def text_of(node: ET.Element, tag: str) -> str:
    child = node.find(tag)
    return "" if child is None else "".join(child.itertext()).strip()


def clean_title(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip().rstrip(".")


def clean_author(value: str) -> str:
    return re.sub(r"\s+\d{4}$", "", value.strip())


def parse_publications(xml_data: bytes) -> list[Publication]:
    root = ET.fromstring(xml_data)
    publications: list[Publication] = []
    for wrapper in root.findall("./r"):
        if len(wrapper) != 1:
            continue
        entry = wrapper[0]
        year_text = text_of(entry, "year")
        title = clean_title(text_of(entry, "title"))
        if not year_text.isdigit() or not title:
            continue
        authors = tuple(
            (author.attrib.get("pid", ""), clean_author("".join(author.itertext())))
            for author in entry.findall("author")
        )
        if not authors:
            continue
        paper_url = text_of(entry, "ee")
        venue = text_of(entry, "booktitle") or text_of(entry, "journal")
        publications.append(
            Publication(
                key=entry.attrib.get("key", ""),
                entry_type=entry.tag,
                publtype=entry.attrib.get("publtype", ""),
                title=title,
                authors=authors,
                year=int(year_text),
                month=text_of(entry, "month"),
                venue=venue,
                volume=text_of(entry, "volume"),
                number=text_of(entry, "number"),
                pages=text_of(entry, "pages"),
                paper_url=paper_url,
            )
        )
    return publications


def parse_bibtex_entries(bib_data: bytes) -> dict[str, str]:
    """Split DBLP's person-level BibTeX export into records keyed by DBLP key."""
    text = bib_data.decode("utf-8")
    starts = list(re.finditer(r"(?m)^@\w+\{DBLP:([^,]+),", text))
    entries: dict[str, str] = {}
    for index, match in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(text)
        entry = text[match.start():end].strip()
        if entry:
            entries[match.group(1)] = entry
    return entries


def normalized_title(title: str) -> str:
    folded = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    return "".join(character.lower() for character in folded if character.isalnum())


def quality(publication: Publication) -> tuple[int, int, int]:
    formal = publication.publtype != "informal" and publication.venue != "CoRR"
    type_rank = 2 if publication.entry_type == "inproceedings" else 1
    return (1 if formal else 0, publication.year, type_rank)


def deduplicate(publications: Iterable[Publication]) -> list[Publication]:
    selected: dict[str, Publication] = {}
    for publication in publications:
        key = normalized_title(publication.title)
        if key not in selected or quality(publication) > quality(selected[key]):
            selected[key] = publication
    return sorted(selected.values(), key=lambda item: (item.year, item.title), reverse=True)


def slugify(value: str) -> str:
    folded = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", folded).strip("-").lower()
    return slug[:90] or "publication"


def publication_date(publication: Publication, override: dict) -> str:
    if override.get("date"):
        return override["date"]
    month = MONTHS.get(publication.month[:3].lower(), 1)
    return f"{publication.year:04d}-{month:02d}-01"


def category_for(publication: Publication) -> str:
    if publication.publtype == "informal" or publication.venue == "CoRR":
        return "preprints"
    if publication.entry_type in {"inproceedings", "proceedings"}:
        return "conferences"
    return "manuscripts"


def venue_for(publication: Publication) -> str:
    if publication.venue == "CoRR":
        identifier = publication.volume.replace("abs/", "arXiv:")
        return f"arXiv preprint {identifier}".strip()
    return publication.venue or "Publication indexed by DBLP"


def join_authors(authors: list[str]) -> str:
    if len(authors) == 1:
        return authors[0]
    if len(authors) == 2:
        return f"{authors[0]} and {authors[1]}"
    return ", ".join(authors[:-1]) + f", and {authors[-1]}"


def compact_pages(pages: str) -> str:
    match = re.fullmatch(r"([^:]+):\d+-\1:\d+", pages)
    return match.group(1) if match else pages.replace("-", "–")


def abbreviated_name(name: str) -> str:
    parts = name.split()
    if len(parts) < 2:
        return name
    initials = " ".join(f"{part[0].upper()}." for part in parts[:-1] if part)
    return f"{initials} {parts[-1]}"


def citation_for(
    publication: Publication,
    title: str,
    venue: str,
    target_pid: str,
    override: dict,
) -> str:
    overridden_authors = override.get("citation_authors")
    authors = []
    for index, (pid, name) in enumerate(publication.authors):
        display_name = (
            overridden_authors[index]
            if overridden_authors and index < len(overridden_authors)
            else abbreviated_name(name)
        )
        escaped = html.escape(display_name, quote=False)
        authors.append(f"<strong>{escaped}</strong>" if pid == target_pid else escaped)

    citation_venue = override.get("citation_venue") or venue
    citation = (
        f"{', '.join(authors)}, &ldquo;{html.escape(title, quote=False)}&rdquo;, "
        f"<i>{html.escape(citation_venue, quote=False)}</i>."
    )
    if override.get("venue_rank"):
        citation += f" ({html.escape(override['venue_rank'], quote=False)})"
    return citation


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def render_publication(
    publication: Publication,
    override: dict,
    target_pid: str,
    bibtex: str = "",
) -> tuple[str, dict]:
    title = override.get("title") or publication.title
    date = publication_date(publication, override)
    slug = override.get("slug") or slugify(title)
    filename = override.get("filename") or f"{date}-{slug}.md"
    permalink = override.get("permalink") or f"/publication/{slug}"
    category = override.get("category") or category_for(publication)
    venue = override.get("venue") or venue_for(publication)
    paper_url = override.get("paperurl") or publication.paper_url
    excerpt = override.get("excerpt") or "Publication metadata synchronized automatically from DBLP."
    abstract = override.get("abstract") or override.get("description") or (
        "Abstract not yet available. Please follow the paper link for the latest details."
    )
    image = (
        override["image"]
        if "image" in override
        else ""
    )
    image_alt = (
        override["image_alt"]
        if "image_alt" in override
        else ""
    )
    authors = override.get("authors") or join_authors([name for _, name in publication.authors])
    author_links = override.get("author_links") or [
        {
            "name": name,
            "url": f"https://dblp.org/pid/{pid}" if pid else "",
            "affiliation": "",
        }
        for pid, name in publication.authors
    ]
    description = override.get("description") or (
        "This publication entry is synchronized automatically from DBLP. "
        "Please follow the links below for the latest bibliographic details."
    )
    links = override.get("links") or []
    if not links:
        if paper_url:
            links.append({"label": "Paper", "url": paper_url})
        links.append({"label": "DBLP", "url": f"https://dblp.org/rec/{publication.key}"})

    front_matter = [
        "---",
        f"title: {yaml_string(title)}",
        "collection: publications",
        f"category: {category}",
        f"permalink: {permalink}",
        f"excerpt: {yaml_string(excerpt)}",
        f"date: {date}",
        f"venue: {yaml_string(venue)}",
        f"paperurl: {yaml_string(paper_url)}",
        f"authors: {yaml_string(authors)}",
        f"author_links: {json.dumps(author_links, ensure_ascii=False)}",
        f"abstract: {yaml_string(abstract)}",
        f"image: {yaml_string(image)}",
        f"image_alt: {yaml_string(image_alt)}",
        f"links: {json.dumps(links, ensure_ascii=False)}",
        f"citation: {yaml_string(citation_for(publication, title, venue, target_pid, override))}",
        f"dblp_key: {yaml_string(publication.key)}",
        f"generated_by: {GENERATED_BY}",
    ]
    curated_bibtex = override.get("bibtex")
    if isinstance(curated_bibtex, list):
        curated_bibtex = "\n".join(curated_bibtex)
    display_bibtex = curated_bibtex or bibtex
    if display_bibtex:
        front_matter.append("bibtex: |-")
        front_matter.extend(f"  {line}" for line in display_bibtex.splitlines())
    front_matter.extend(
        [
            "---",
            "",
            description.strip(),
            "",
            " ".join(f"[[{item['label']}]]({item['url']})" for item in links),
            "",
        ]
    )
    news_venue = override.get("news_venue") or override.get("citation_venue") or venue
    news = {
        "date": date,
        "date_label": override.get("news_date") or date[:7].replace("-", "."),
        "text": override.get("news_text") or f"🎉 One paper is published in {news_venue}",
        "show": override.get("show_in_news", True),
    }
    return "\n".join(front_matter), {"filename": filename, "news": news}


def load_overrides(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def render_news(items: list[dict]) -> str:
    lines = ["# Generated by scripts/sync_publications.py. Do not edit manually."]
    visible_items = [item for item in items if item["show"]]
    for item in sorted(visible_items, key=lambda value: value["date"], reverse=True)[:5]:
        lines.extend(
            [
                f"- date: {yaml_string(item['date_label'])}",
                f"  text: {yaml_string(item['text'])}",
            ]
        )
    return "\n".join(lines) + "\n"


def update_heartbeat(root: Path, interval_days: int = 45) -> bool:
    """Record occasional successful checks so GitHub does not disable the schedule."""
    path = root / "_data" / "publication_sync.json"
    today = date.today()
    if path.exists():
        try:
            previous = date.fromisoformat(json.loads(path.read_text(encoding="utf-8"))["last_checked"])
            if (today - previous).days < interval_days:
                return False
        except (KeyError, ValueError, json.JSONDecodeError):
            pass
    path.write_text(
        json.dumps({"last_checked": today.isoformat()}, indent=2) + "\n",
        encoding="utf-8",
    )
    return True


def sync(
    root: Path,
    publications: list[Publication],
    target_pid: str,
    bibtex_entries: dict[str, str] | None = None,
) -> tuple[int, int]:
    if not publications:
        raise RuntimeError("DBLP returned no publications; refusing to modify the site")
    if not any(pid == target_pid for publication in publications for pid, _ in publication.authors):
        raise RuntimeError("DBLP data does not contain the configured author PID")

    overrides = load_overrides(root / "_data" / "publication_overrides.json")
    output_dir = root / "_publications"
    output_dir.mkdir(parents=True, exist_ok=True)
    expected: set[Path] = set()
    news_items: list[dict] = []
    bibtex_entries = bibtex_entries or {}

    for publication in deduplicate(publications):
        content, metadata = render_publication(
            publication,
            overrides.get(publication.key, {}),
            target_pid,
            bibtex_entries.get(publication.key, ""),
        )
        path = output_dir / metadata["filename"]
        path.write_text(content, encoding="utf-8")
        expected.add(path.resolve())
        news_items.append(metadata["news"])

    removed = 0
    for path in output_dir.glob("*.md"):
        if path.resolve() in expected:
            continue
        if f"generated_by: {GENERATED_BY}" in path.read_text(encoding="utf-8", errors="ignore"):
            path.unlink()
            removed += 1

    (root / "_data" / "auto_news.yml").write_text(render_news(news_items), encoding="utf-8")
    update_heartbeat(root)
    return len(expected), removed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", default=os.environ.get("DBLP_SOURCE", DEFAULT_SOURCE))
    parser.add_argument(
        "--bib-source",
        default=os.environ.get("DBLP_BIB_SOURCE", DEFAULT_BIB_SOURCE),
    )
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--pid", default=DEFAULT_DBLP_PID)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        records = parse_publications(fetch_source(args.source))
        bibtex_entries = parse_bibtex_entries(
            fetch_source(args.bib_source, accept="application/x-bibtex")
        )
        written, removed = sync(args.root.resolve(), records, args.pid, bibtex_entries)
    except Exception as error:  # Surface a concise message in GitHub Actions logs.
        print(f"Publication sync failed: {error}", file=sys.stderr)
        return 1
    print(f"Synchronized {written} publications; removed {removed} stale generated entries.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
