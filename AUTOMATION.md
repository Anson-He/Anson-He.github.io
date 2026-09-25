# Publication and News Automation

The homepage synchronizes publication metadata from Yuhao He's public DBLP record:

- Source: `https://dblp.org/pid/257/8328-1.xml`
- Fallback: official DBLP SPARQL endpoint at `https://sparql.dblp.org/sparql`
- Schedule: every day at 02:17 UTC
- Manual run: **Actions → Sync publications from DBLP → Run workflow**

The workflow runs `scripts/sync_publications.py` and checks `_publications/` and
`_data/auto_news.yml` for changes. Existing reviewed records remain visible.
If DBLP's XML or BibTeX endpoint serves a browser-verification page, the script
automatically reads the same curated DBLP records through the official SPARQL
endpoint instead.
Every newly discovered record is generated with `visible: false`, is excluded
from the homepage, publication archive, CV, and automatic News, and is staged in
a draft pull request instead of being pushed directly to the live site.

The workflow assigns the draft pull request to the GitHub user `Anson-He` and
mentions that account in the pull-request body. GitHub therefore sends a review
notification to the email configured for repository notifications. To publish a
record, verify its metadata in **Files changed**, edit its publication file from
`visible: false` to `visible: true`, mark the pull request ready, and merge it.
To reject a record or keep it hidden, leave `visible: false` unchanged and merge
the pull request; this records the decision so it will not trigger another daily
reminder. Closing without merging causes the DBLP record to be rediscovered.

Formal conference or journal records take priority over duplicate preprints.
Curated, citation-ready BibTeX from publisher, DOI, or arXiv metadata takes
priority over DBLP's person-level BibTeX export, which remains the fallback for
newly discovered records.

GitHub can disable scheduled workflows in inactive public repositories. A small
`_data/publication_sync.json` heartbeat is therefore updated at most once every
45 days, keeping the schedule active without creating daily no-op commits.

Curated descriptions, stable permalinks, and extra links are stored in
`_data/publication_overrides.json`. Add a record there when a new publication
needs a custom abstract, paper figure, code link, shorter venue name, author
initials, citation-ready BibTeX, or acceptance-style news text. An explicit empty
`image` value disables the figure for that publication. New DBLP records are
prepared automatically with a neutral image and an abstract placeholder, but
stay off the live site until reviewed. Automatic News is generated only for
visible publications.

Non-publication updates can be added to `_data/manual_news.yml`; the synchronizer
does not overwrite that file.
