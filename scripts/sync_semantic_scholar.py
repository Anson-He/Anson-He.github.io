#!/usr/bin/env python3
"""Append newly discovered Semantic Scholar papers for manual review."""

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
import urllib.parse
import urllib.request
from pathlib import Path


DEFAULT_AUTHOR_ID = "2330150098"
FIELDS = (
    "paperId,title,authors,year,venue,publicationDate,externalIds,"
    "openAccessPdf,url"
)
USER_AGENT = (
    "Anson-He-Academic-Homepage/3.0 "
    "(mailto:3250004430@student.must.edu.mo)"
)
GENERATED_BY = "semantic_scholar_sync"


def api_url(author_id: str) -> str:
    query = urllib.parse.urlencode({"fields": FIELDS, "limit": 1000})
    return (
        "https://api.semanticscholar.org/graph/v1/author/"
        f"{author_id}/papers?{query}"
    )


def fetch_papers(source: str, api_key: str = "") -> list[dict]:
    if not source.startswith(("http://", "https://")):
        payload = json.loads(Path(source).read_text(encoding="utf-8"))
        return validate_payload(payload)

    headers = {"Accept": "application/json", "User-Agent": USER_AGENT}
    if api_key:
        headers["x-api-key"] = api_key
    request = urllib.request.Request(source, headers=headers)

    for attempt in range(1, 6):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return validate_payload(json.load(response))
        except urllib.error.HTTPError as error:
            if error.code != 429 and error.code < 500:
                raise
            if attempt == 5:
                raise
            retry_after = error.headers.get("Retry-After")
            wait = min(int(retry_after), 60) if retry_after and retry_after.isdigit() else 2**attempt * 2
            print(
                f"Semantic Scholar returned {error.code}; retrying in {wait}s...",
                file=sys.stderr,
            )
            time.sleep(wait)
        except urllib.error.URLError:
            if attempt == 5:
                raise
            time.sleep(2**attempt)
    raise RuntimeError("Semantic Scholar request failed after retries")


def validate_payload(payload: dict) -> list[dict]:
    papers = payload.get("data")
    if not isinstance(papers, list):
        raise ValueError("Unexpected Semantic Scholar response: no data array")
    return papers


def normalized_title(title: str) -> str:
    folded = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    return "".join(character.lower() for character in folded if character.isalnum())


def slugify(value: str) -> str:
    folded = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", folded).strip("-").lower()
    return slug[:90] or "publication"


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def clean_date(paper: dict) -> str:
    publication_date = paper.get("publicationDate") or ""
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", publication_date):
        return publication_date
    year = paper.get("year")
    return f"{int(year):04d}-01-01" if isinstance(year, int) else "1900-01-01"


def join_authors(authors: list[str]) -> str:
    if len(authors) == 1:
        return authors[0]
    if len(authors) == 2:
        return f"{authors[0]} and {authors[1]}"
    return ", ".join(authors[:-1]) + f", and {authors[-1]}"


def abbreviated_name(name: str) -> str:
    parts = name.split()
    if len(parts) < 2:
        return name
    initials = " ".join(f"{part[0].upper()}." for part in parts[:-1] if part)
    return f"{initials} {parts[-1]}"


def links_for(paper: dict) -> tuple[str, list[dict]]:
    external_ids = paper.get("externalIds") or {}
    doi = external_ids.get("DOI")
    arxiv = external_ids.get("ArXiv")
    dblp = external_ids.get("DBLP")
    semantic_url = paper.get("url") or (
        f"https://www.semanticscholar.org/paper/{paper['paperId']}"
    )
    open_pdf = (paper.get("openAccessPdf") or {}).get("url")

    if doi:
        paper_url = f"https://doi.org/{doi}"
    elif arxiv:
        paper_url = f"https://arxiv.org/abs/{arxiv}"
    elif open_pdf:
        paper_url = open_pdf
    else:
        paper_url = semantic_url

    links = [{"label": "Paper", "url": paper_url}]
    if arxiv:
        arxiv_url = f"https://arxiv.org/abs/{arxiv}"
        if arxiv_url != paper_url:
            links.append({"label": "arXiv", "url": arxiv_url})
    if dblp:
        links.append({"label": "DBLP", "url": f"https://dblp.org/rec/{dblp}"})
    links.append({"label": "Semantic Scholar", "url": semantic_url})
    return paper_url, links


def render_candidate(paper: dict, author_id: str) -> tuple[str, str]:
    title = str(paper.get("title") or "Untitled").strip()
    date = clean_date(paper)
    paper_id = str(paper["paperId"])
    slug = slugify(title)
    filename = f"{date}-{slug}.md"
    venue = str(paper.get("venue") or "Preprint")
    external_ids = paper.get("externalIds") or {}
    doi = str(external_ids.get("DOI") or "").lower()
    category = (
        "preprints"
        if external_ids.get("ArXiv") and (not doi or "10.48550/arxiv" in doi)
        else "manuscripts"
    )
    paper_url, links = links_for(paper)

    author_records = paper.get("authors") or []
    author_names = [str(author.get("name") or "Unknown") for author in author_records]
    authors = join_authors(author_names)
    citation_authors = []
    for author in author_records:
        name = html.escape(abbreviated_name(str(author.get("name") or "Unknown")))
        if str(author.get("authorId") or "") == author_id:
            name = f"<strong>{name}</strong>"
        citation_authors.append(name)
    citation = (
        f"{', '.join(citation_authors)}, &ldquo;{html.escape(title)}&rdquo;, "
        f"<i>{html.escape(venue)}</i>."
    )
    dblp_key = str(external_ids.get("DBLP") or "")
    placeholder = (
        "This record was discovered automatically through Semantic Scholar. "
        "Please verify the authorship and bibliographic metadata before publishing it."
    )

    front_matter = [
        "---",
        f"title: {yaml_string(title)}",
        "collection: publications",
        f"category: {category}",
        f"permalink: /publication/{slug}",
        f"excerpt: {yaml_string(placeholder)}",
        f"date: {date}",
        f"venue: {yaml_string(venue)}",
        f"paperurl: {yaml_string(paper_url)}",
        f"authors: {yaml_string(authors)}",
        f"abstract: {yaml_string(placeholder)}",
        'image: ""',
        'image_alt: ""',
        f"links: {json.dumps(links, ensure_ascii=False)}",
        f"citation: {yaml_string(citation)}",
        f"dblp_key: {yaml_string(dblp_key)}",
        f"semantic_scholar_id: {yaml_string(paper_id)}",
        "visible: false",
        f"generated_by: {GENERATED_BY}",
        "---",
        "",
        placeholder,
        "",
        " ".join(f"[[{item['label']}]]({item['url']})" for item in links),
        "",
    ]
    return filename, "\n".join(front_matter)


def existing_records(output_dir: Path) -> tuple[set[str], set[str]]:
    paper_ids: set[str] = set()
    titles: set[str] = set()
    for path in output_dir.glob("*.md"):
        content = path.read_text(encoding="utf-8", errors="ignore")
        id_match = re.search(
            r'^semantic_scholar_id:\s*"([^"]+)"\s*$', content, re.MULTILINE
        )
        title_match = re.search(r'^title:\s*"(.*)"\s*$', content, re.MULTILINE)
        if id_match:
            paper_ids.add(id_match.group(1))
        if title_match:
            try:
                title = json.loads(f'"{title_match.group(1)}"')
            except json.JSONDecodeError:
                title = title_match.group(1)
            titles.add(normalized_title(title))
    return paper_ids, titles


def sync(root: Path, papers: list[dict], author_id: str) -> list[dict]:
    output_dir = root / "_publications"
    output_dir.mkdir(parents=True, exist_ok=True)
    known_ids, known_titles = existing_records(output_dir)
    added = []

    for paper in papers:
        paper_id = str(paper.get("paperId") or "")
        title = str(paper.get("title") or "")
        if not paper_id or not title:
            continue
        if paper_id in known_ids or normalized_title(title) in known_titles:
            continue
        filename, content = render_candidate(paper, author_id)
        path = output_dir / filename
        if path.exists():
            path = output_dir / f"{path.stem}-{paper_id[:8]}.md"
        path.write_text(content, encoding="utf-8")
        known_ids.add(paper_id)
        known_titles.add(normalized_title(title))
        added.append({"paper_id": paper_id, "title": title, "year": paper.get("year")})

    return added


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--author-id", default=DEFAULT_AUTHOR_ID)
    parser.add_argument("--source", default=os.environ.get("SEMANTIC_SCHOLAR_SOURCE"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.source or api_url(args.author_id)
    try:
        papers = fetch_papers(source, os.environ.get("SEMANTIC_SCHOLAR_API_KEY", ""))
        added = sync(args.root.resolve(), papers, args.author_id)
    except Exception as error:
        print(f"Semantic Scholar sync failed: {error}", file=sys.stderr)
        return 1

    print(f"Semantic Scholar returned {len(papers)} papers.")
    if not added:
        print("No new papers; the publication collection is unchanged.")
        return 0
    print(f"Added {len(added)} paper(s) with visible: false:")
    for item in added:
        print(f"  - [{item['year'] or 'n.d.'}] {item['title']} ({item['paper_id']})")
    print("Review each record and set visible: true before publishing it.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
