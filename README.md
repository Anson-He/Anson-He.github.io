# Yuhao He's Academic Homepage

Academic homepage for [Yuhao He](https://anson-he.github.io/), with a responsive sidebar and publication-card design adapted from boyugou’s academic homepage template, retaining Jekyll data collections.

## Content

- `_pages/about.md`: single-page homepage
- `_pages/cv.md`: web CV
- `_publications/`: publication metadata rendered on the homepage and archive
- `_data/publication_overrides.json`: curated abstracts, links, images, and BibTeX
- `scripts/sync_semantic_scholar.py`: review-gated Semantic Scholar discovery
- `assets/css/academic.css`: light/dark site theme
- `assets/js/academic.js`: theme switching and production visitor counter

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

## Design credits

The sidebar layout, theme tokens and publication card styles are adapted from [boyugou/academic-homepage-template](https://github.com/boyugou/academic-homepage-template) (MIT). The license is retained in `assets/vendor/academic-homepage-template-LICENSE.txt`. Content continues to use Jekyll collections and the existing review-gated publication workflow.

## Visitor counter

The production site loads Busuanzi to display site-wide page views and visitors in the footer. Local previews do not load the counter; unavailable values are shown as a dash rather than fabricated counts. GoatCounter is no longer loaded.
