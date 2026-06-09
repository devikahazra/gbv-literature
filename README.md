# Gender-Based Violence — Literature Review

A structured bibliography of papers on gender-based violence. Each entry is
catalogued along a fixed schema — identification strategy, outcome, methods,
data, and how it relates to ongoing work — so the literature is searchable and
comparable at a glance rather than a flat reading list.

The master data lives in [`data/papers.csv`](data/papers.csv). The table below is
generated from it; see the [Field Guide](FIELD_GUIDE.md) for what each column
means and how to add a paper.

## Interactive browser

[`index.html`](index.html) is a self-contained page that reads the same CSV and
renders it as a searchable, filterable, sortable table — click any row to expand
the full record. To publish it: in your repo, go to **Settings → Pages**, set the
source to your default branch, and the page goes live at
`https://<username>.github.io/<repo>/`. (Opening `index.html` straight from disk
won't auto-load the CSV — use Pages, or run `python -m http.server` locally, or
use the page's manual file-picker fallback.)

## Schema

`No` · `Authors` · `Title` · `Year` · `Journal` · `Identification Shock` ·
`Outcome` · `Methods` · `Main Results` · `Theoretical Framework` ·
`Data Source` · `Group Type` · `Context` · `Country` · `Gap/Difference`

## Adding papers

1. Add a row to `data/papers.csv` (quote any cell containing a comma).
2. Run `python scripts/build_readme.py` to refresh the table below.
3. Commit and push.

## Papers

<!-- TABLE:START -->

| No | Authors | Title | Year | Journal | Identification Shock | Outcome | Methods | Main Results | Theoretical Framework | Data Source | Group Type | Context | Country | Gap/Difference |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Hazra | Does a Centralized Emergency Response System Increase Crime Reporting Among Minorities? – Evidence from India | 2023 | WP | Law Enforcement | Crime Reporting | Staggered DiD | Increased reporting among caste-based minorities | Becker's Model | NCRB, Census, BPRD | Caste-Based | Crime/Discrimination | India | Sample row — replace with GBV papers |

**1 paper listed.**

<!-- TABLE:END -->
