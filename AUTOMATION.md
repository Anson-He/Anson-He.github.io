# Publication Review Automation

The homepage follows the review-gated Semantic Scholar workflow used by Drew
Dimmery's website.

- Source: Semantic Scholar author `2330150098`
- Schedule: Mondays at 06:15 UTC
- Manual run: **Actions → Sync papers from Semantic Scholar → Run workflow**
- Optional secret: `SEMANTIC_SCHOLAR_API_KEY` for a higher API rate limit

The workflow runs `scripts/sync_semantic_scholar.py`. It compares Semantic
Scholar paper IDs with the IDs already stored in `_publications/`, and only
appends records it has not seen before. It never overwrites or reorders reviewed
publication files.

Every newly discovered record is created with `visible: false`. Hidden records
are excluded from the homepage, publication archive, web CV, and automatic News.
The workflow puts the candidates in a draft pull request, assigns the pull
request to `Anson-He`, and mentions that account in the body. GitHub then sends a
review notification to the email configured for repository notifications.

To approve a paper, verify the title, authors, venue, year, and links in **Files
changed**. Replace the placeholder with the official abstract, add
publisher/arXiv BibTeX when available, change `visible: false` to `visible:
true`, mark the pull request ready, and merge it. Curated presentation fields
can be added to `_data/publication_overrides.json` when needed.

To reject a paper or keep it hidden, leave `visible: false` unchanged and merge
the pull request. This stores its Semantic Scholar paper ID and prevents it from
triggering another weekly reminder. Closing without merging causes the same
record to be rediscovered later.

An unreviewed candidate that has been merged into `main` is automatically
archived after 14 days. Its Markdown file is removed from `_publications/`, and its paper ID is stored in
`_data/semantic_scholar_ignored.json`, so the same record is not rediscovered.
Candidates changed to `visible: true` are never archived.

Semantic Scholar sometimes merges different researchers who share the same
name. The review gate is therefore intentional: discovery is automatic, but
publication is always a human decision.

Non-publication announcements remain in `_data/manual_news.yml`. The discovery
workflow does not infer acceptance announcements from bibliographic metadata.
