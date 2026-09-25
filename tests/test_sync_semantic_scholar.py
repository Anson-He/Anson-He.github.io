import sys
import tempfile
import unittest
from datetime import date, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import sync_semantic_scholar as sync  # noqa: E402


def sample_paper(paper_id="new-paper", title="A Newly Discovered Paper"):
    return {
        "paperId": paper_id,
        "title": title,
        "year": 2026,
        "publicationDate": "2026-09-01",
        "venue": "Example Conference",
        "authors": [
            {"authorId": sync.DEFAULT_AUTHOR_ID, "name": "Yuhao He"},
            {"authorId": "42", "name": "Jinyu Tian"},
        ],
        "externalIds": {
            "ArXiv": "2609.00001",
            "DOI": "10.48550/arXiv.2609.00001",
        },
        "openAccessPdf": {"url": "https://arxiv.org/pdf/2609.00001"},
        "url": "https://www.semanticscholar.org/paper/new-paper",
    }


class SemanticScholarSyncTests(unittest.TestCase):
    def test_renders_new_paper_hidden_with_review_metadata(self):
        filename, content = sync.render_candidate(
            sample_paper(), sync.DEFAULT_AUTHOR_ID
        )
        self.assertEqual(filename, "2026-09-01-a-newly-discovered-paper.md")
        self.assertIn("visible: false", content)
        self.assertIn('semantic_scholar_id: "new-paper"', content)
        self.assertIn("<strong>Y. He</strong>", content)
        self.assertIn("https://arxiv.org/abs/2609.00001", content)

    def test_sync_only_appends_unknown_papers(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output_dir = root / "_publications"
            output_dir.mkdir()
            (output_dir / "existing.md").write_text(
                '---\ntitle: "Existing Paper"\n'
                'semantic_scholar_id: "known-id"\nvisible: true\n---\n',
                encoding="utf-8",
            )
            papers = [
                sample_paper("known-id", "Existing Paper"),
                sample_paper("duplicate-title", "Existing Paper"),
                sample_paper(),
            ]
            added = sync.sync(root, papers, sync.DEFAULT_AUTHOR_ID)
            self.assertEqual([item["paper_id"] for item in added], ["new-paper"])
            self.assertEqual(len(list(output_dir.glob("*.md"))), 2)
            self.assertIn(
                "visible: true",
                (output_dir / "existing.md").read_text(encoding="utf-8"),
            )

    def test_invalid_api_shape_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "no data array"):
            sync.validate_payload({"error": "rate limited"})

    def test_stale_hidden_candidates_are_archived_and_ignored(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output_dir = root / "_publications"
            output_dir.mkdir()
            (root / "_data").mkdir()
            stale_date = date(2026, 9, 1)
            (output_dir / "stale.md").write_text(
                "---\n"
                'title: "Stale Candidate"\n'
                'semantic_scholar_id: "stale-id"\n'
                f'discovered_at: "{stale_date.isoformat()}"\n'
                "visible: false\n"
                "generated_by: semantic_scholar_sync\n"
                "---\n",
                encoding="utf-8",
            )
            removed = sync.prune_stale(root, date(2026, 9, 25))
            self.assertEqual(removed[0]["paper_id"], "stale-id")
            self.assertFalse((output_dir / "stale.md").exists())
            ignored = sync.load_ignored(root / "_data" / sync.IGNORED_FILENAME)
            self.assertIn("stale-id", ignored)
            self.assertEqual(sync.sync(root, [sample_paper("stale-id")], sync.DEFAULT_AUTHOR_ID), [])

    def test_recent_hidden_candidates_are_not_archived(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            output_dir = root / "_publications"
            output_dir.mkdir()
            recent_date = date(2026, 9, 20)
            _, content = sync.render_candidate(
                sample_paper("recent-id"), sync.DEFAULT_AUTHOR_ID, recent_date
            )
            (output_dir / "recent.md").write_text(content, encoding="utf-8")
            self.assertEqual(sync.prune_stale(root, date(2026, 9, 25)), [])
            self.assertTrue((output_dir / "recent.md").exists())


if __name__ == "__main__":
    unittest.main()
