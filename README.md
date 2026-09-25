# Yuhao He's Academic Homepage

Minimal academic homepage for [Yuhao He](https://anson-he.github.io/), inspired by the visual simplicity of Jemdoc while retaining Jekyll data collections.

## Content

- `_pages/about.md`: single-page homepage
- `_pages/cv.md`: web CV
- `_publications/`: publication metadata rendered on the homepage and archive
- `_data/publication_overrides.json`: curated abstracts, links, images, and BibTeX
- `scripts/sync_publications.py`: DBLP publication and news synchronizer
- `assets/css/jemdoc.css`: complete site theme

## Automatic publication updates

The `Sync publications from DBLP` GitHub Actions workflow runs daily. It reads Yuhao He's DBLP record, falls back to DBLP's official SPARQL endpoint when the XML service presents a bot-verification page, and opens an assigned draft pull request when it finds changes. New publications are marked `visible: false` and remain off the live homepage until Yuhao reviews the metadata, changes the flag to `true`, and merges the pull request. The assignment uses GitHub's normal notification email, so no email password is stored in the repository.

## Local preview

```bash
bundle install
bundle exec jekyll serve
```

Then open `http://127.0.0.1:4000/`.
