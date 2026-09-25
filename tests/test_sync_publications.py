import sys
import tempfile
import unittest
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import sync_publications as sync  # noqa: E402


class SyncPublicationsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture = ROOT / "tests" / "fixtures" / "dblp-yuhao.xml"
        cls.records = sync.parse_publications(fixture.read_bytes())
        bib_fixture = ROOT / "tests" / "fixtures" / "dblp-yuhao.bib"
        cls.bibtex_entries = sync.parse_bibtex_entries(bib_fixture.read_bytes())

    def test_parses_all_dblp_records(self):
        self.assertEqual(len(self.records), 4)

    def test_prefers_formal_publication_over_preprint(self):
        selected = sync.deduplicate(self.records)
        self.assertEqual(len(selected), 3)
        deferred = next(item for item in selected if item.title.startswith("Deferred Poisoning"))
        self.assertEqual(deferred.key, "conf/aaai/HeTZDLZ26")

    def test_compacts_article_number_pages(self):
        self.assertEqual(sync.compact_pages("2250058:1-2250058:26"), "2250058")

    def test_author_disambiguation_suffixes_are_removed(self):
        deferred = self.records[0]
        self.assertEqual(deferred.authors[0][1], "Yuhao He")
        self.assertEqual(deferred.authors[1][1], "Jinyu Tian")

    def test_parses_official_bibtex_by_dblp_key(self):
        self.assertEqual(len(self.bibtex_entries), 4)
        entry = self.bibtex_entries["journals/ijwmip/HeZM23"]
        self.assertIn("@article{DBLP:journals/ijwmip/HeZM23", entry)
        self.assertIn("10.1142/S0219691322500588", entry)

    def test_parses_sparql_fallback_and_preserves_author_order(self):
        def binding(value):
            return {"type": "literal", "value": str(value)}

        rows = []
        for ordinal, pid, name in [
            (1, "257/8328-1", "Yuhao He 0001"),
            (2, "14/1023-1", "Jinyu Tian 0001"),
        ]:
            rows.append(
                {
                    "pub": binding("https://dblp.org/rec/conf/test/HeT26"),
                    "bibtexType": binding(
                        "http://purl.org/net/nknouf/ns/bibtex#Inproceedings"
                    ),
                    "title": binding("A Test Paper."),
                    "year": binding("2026"),
                    "month": binding("--05"),
                    "venue": binding("TestConf"),
                    "pages": binding("1-9"),
                    "paperUrl": binding("https://doi.org/10.0000/test"),
                    "author": binding(f"https://dblp.org/pid/{pid}"),
                    "authorName": binding(name),
                    "ordinal": binding(ordinal),
                    "informal": binding("false"),
                }
            )
        payload = json.dumps({"results": {"bindings": rows}}).encode()
        parsed = sync.parse_sparql_publications(payload)
        self.assertEqual(len(parsed), 1)
        self.assertEqual(parsed[0].key, "conf/test/HeT26")
        self.assertEqual(parsed[0].entry_type, "inproceedings")
        self.assertEqual(parsed[0].month, "may")
        self.assertEqual(
            parsed[0].authors,
            (("257/8328-1", "Yuhao He"), ("14/1023-1", "Jinyu Tian")),
        )

    def test_compact_citation_uses_curated_initials_and_bolds_owner(self):
        publication = next(
            item for item in self.records if item.key == "conf/aaai/HeTZDLZ26"
        )
        override = {
            "citation_authors": [
                "Y. H. He",
                "J. Y. Tian",
                "X. W. Zheng",
                "L. Dong",
                "Y. M. Li",
                "J. T. Zhou",
            ],
            "citation_venue": "AAAI",
            "venue_rank": "CCF A",
        }
        citation = sync.citation_for(
            publication,
            publication.title,
            publication.venue,
            sync.DEFAULT_DBLP_PID,
            override,
        )
        self.assertTrue(citation.startswith("<strong>Y. H. He</strong>, J. Y. Tian"))
        self.assertIn("<i>AAAI</i>. (CCF A)", citation)

    def test_news_rendering_uses_date_and_acceptance_style(self):
        rendered = sync.render_news(
            [
                {
                    "date": "2026-01-01",
                    "date_label": "2025.11",
                    "text": "🎉 One paper is accepted by AAAI 2026",
                    "show": True,
                },
                {
                    "date": "2025-05-27",
                    "date_label": "2025.05",
                    "text": "hidden",
                    "show": False,
                },
            ]
        )
        self.assertIn('date: "2025.11"', rendered)
        self.assertIn("One paper is accepted by AAAI 2026", rendered)
        self.assertNotIn("hidden", rendered)

    def test_curated_bibtex_overrides_dblp_and_image_can_be_disabled(self):
        publication = next(
            item for item in self.records if item.key == "journals/ijwmip/HeZM23"
        )
        curated = [
            "@article{he2023tfa,",
            "  title = {TFA-CLSTMNN},",
            "  year = {2023}",
            "}",
        ]
        content, _ = sync.render_publication(
            publication,
            {"bibtex": curated, "image": ""},
            sync.DEFAULT_DBLP_PID,
            self.bibtex_entries[publication.key],
        )
        self.assertIn('image: ""', content)
        self.assertIn("@article{he2023tfa", content)
        self.assertNotIn("DBLP:journals/ijwmip/HeZM23", content)

    def test_existing_publications_default_to_visible(self):
        with tempfile.TemporaryDirectory() as directory:
            output_dir = Path(directory)
            (output_dir / "existing.md").write_text(
                '---\ndblp_key: "conf/aaai/HeTZDLZ26"\ngenerated_by: dblp_sync\n---\n',
                encoding="utf-8",
            )
            self.assertTrue(sync.load_visibility(output_dir)["conf/aaai/HeTZDLZ26"])

    def test_new_publications_are_hidden_and_excluded_from_news(self):
        publication = next(
            item for item in self.records if item.key == "journals/ijwmip/HeZM23"
        )
        content, metadata = sync.render_publication(
            publication,
            {},
            sync.DEFAULT_DBLP_PID,
            visible=False,
        )
        self.assertIn("visible: false", content)
        self.assertFalse(metadata["news"]["show"])

    def test_reviewed_publication_remains_visible_after_sync(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "_data").mkdir()
            (root / "_publications").mkdir()
            (root / "_data" / "publication_overrides.json").write_text(
                "{}", encoding="utf-8"
            )
            (root / "_publications" / "reviewed.md").write_text(
                '---\ndblp_key: "journals/ijwmip/HeZM23"\nvisible: true\n'
                'generated_by: dblp_sync\n---\n',
                encoding="utf-8",
            )
            publication = next(
                item for item in self.records if item.key == "journals/ijwmip/HeZM23"
            )
            sync.sync(root, [publication], sync.DEFAULT_DBLP_PID)
            rendered = next((root / "_publications").glob("*.md")).read_text()
            self.assertIn("visible: true", rendered)

    def test_heartbeat_is_not_rewritten_every_run(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "_data").mkdir()
            self.assertTrue(sync.update_heartbeat(root))
            first = (root / "_data" / "publication_sync.json").read_text()
            self.assertFalse(sync.update_heartbeat(root))
            self.assertEqual((root / "_data" / "publication_sync.json").read_text(), first)


if __name__ == "__main__":
    unittest.main()
