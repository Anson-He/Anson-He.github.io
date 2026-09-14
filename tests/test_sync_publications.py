import sys
import tempfile
import unittest
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

    def test_curated_author_links_are_written_to_front_matter(self):
        publication = next(
            item for item in self.records if item.key == "journals/ijwmip/HeZM23"
        )
        author_links = [
            {
                "name": "Yuhao He",
                "url": "https://anson-he.github.io/",
                "affiliation": "Foshan University",
            }
        ]
        content, _ = sync.render_publication(
            publication,
            {"author_links": author_links},
            sync.DEFAULT_DBLP_PID,
        )
        self.assertIn('author_links: [{"name": "Yuhao He"', content)
        self.assertIn('"affiliation": "Foshan University"', content)

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
