# Publication and News Automation

The homepage synchronizes publication metadata from Yuhao He's public DBLP record:

- Source: `https://dblp.org/pid/257/8328-1.xml`
- Schedule: every Monday at 02:17 UTC
- Manual run: **Actions → Sync publications from DBLP → Run workflow**

The workflow runs `scripts/sync_publications.py`, updates `_publications/` and
`_data/auto_news.yml`, and commits only when the generated content changes.
Formal conference or journal records take priority over duplicate preprints.

GitHub can disable scheduled workflows in inactive public repositories. A small
`_data/publication_sync.json` heartbeat is therefore updated at most once every
45 days, keeping the schedule active without creating weekly no-op commits.

Curated descriptions, stable permalinks, and extra links are stored in
`_data/publication_overrides.json`. Add a record there when a new publication
needs a custom abstract, code link, or shorter venue name.

Non-publication updates can be added to `_data/manual_news.yml`; the synchronizer
does not overwrite that file.
