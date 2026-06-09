# Field Guide

Each row in [`data/papers.csv`](data/papers.csv) is one paper. Columns follow the
review schema below. Leave a cell blank if not applicable (e.g. `N/A`, narrative
pieces, working papers without a journal).

| Column | What goes here |
|---|---|
| **No** | Sequential entry number. |
| **Authors** | Last names, comma-separated (e.g. `Aneja, Ritadhi`). |
| **Title** | Full paper title. |
| **Year** | Publication year, or `WP` for an unpublished working paper. |
| **Journal** | Outlet, or `WP` / `Book` / `Blog Piece` etc. |
| **Identification Shock** | The source of variation used for identification (e.g. a policy rollout, an election, a natural experiment). `N/A` for descriptive/narrative work. |
| **Outcome** | The dependent variable / phenomenon studied. |
| **Methods** | Empirical strategy (e.g. `Staggered DiD`, `RD`, `2SLS`, `OLS, FE`, `Narrative`). |
| **Main Results** | One- or two-line summary of the headline finding. |
| **Theoretical Framework** | Theory or model the paper builds on (e.g. `Becker's Model`, `Social Norms`), or `None`. |
| **Data Source** | Datasets used (e.g. `NFHS`, `NCRB`, `Census`, original survey). |
| **Group Type** | The population dimension of interest. For a GBV review this is typically the relevant axis (e.g. `Gender`, `Intra-household`, `Marital status`), but keep whatever value fits the paper. |
| **Context** | Broad theme (e.g. `Crime/Discrimination`, `Development`, `Conflict`, `Political`). |
| **Country** | Country or region of the study. |
| **Gap/Difference** | How this paper relates to your own work — what it leaves open, or how yours differs. Your private notes column. |

## Adding a paper
1. Open `data/papers.csv`, add a row (increment `No`).
2. Wrap any cell containing a comma in double quotes: `"NCRB, Census, BPRD"`.
3. Run `python scripts/build_readme.py` to refresh the table in the README.
4. Commit and push.
