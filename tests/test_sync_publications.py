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
