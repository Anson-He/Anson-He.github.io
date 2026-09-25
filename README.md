# Yuhao He's Academic Homepage

Minimal academic homepage for [Yuhao He](https://anson-he.github.io/), inspired by the visual simplicity of Jemdoc while retaining Jekyll data collections.

## Content

- `_pages/about.md`: single-page homepage
- `_pages/cv.md`: web CV
- `_publications/`: publication metadata rendered on the homepage and archive
- `_data/publication_overrides.json`: curated abstracts, links, images, and BibTeX
- `scripts/sync_semantic_scholar.py`: review-gated Semantic Scholar discovery
- `assets/css/jemdoc.css`: complete site theme

## Automatic publication updates

The `Sync papers from Semantic Scholar` GitHub Actions workflow runs every Monday. It checks Semantic Scholar author `2330150098` and only appends previously unseen paper IDs. New records are marked `visible: false` and remain off the live homepage until Yuhao reviews the metadata, changes the flag to `true`, and merges the assigned draft pull request. The assignment uses GitHub's normal notification email, so no email password is stored in the repository.

Unreviewed hidden candidates are archived automatically after 14 days. Their IDs
are retained in `_data/semantic_scholar_ignored.json` to prevent repeat alerts.

## Local preview

```bash
bundle install
bundle exec jekyll serve
```

Then open `http://127.0.0.1:4000/`.
