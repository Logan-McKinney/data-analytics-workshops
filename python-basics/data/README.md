# Local MLB teaching data

The original `mlb_2026_hitters.csv` is excluded because redistribution permission was not established. Place an authorized local copy in this folder under that name to run the data-analysis sections. This folder's CSV/JSON files are ignored by Git.

Expected columns:

```text
Player,Team,League,Position,G,AB,R,H,2B,3B,HR,RBI,BB,SO,SB,CS,AVG,OBP,SLG,OPS
```

Counting and rate statistics should be numeric. The verification script expects the original teaching sample's shape: 50 rows, 20 columns, with 25 AL and 25 NL records. It can check an authorized copy without adding it to the repository:

```sh
python scripts/verify_notebooks.py --mlb-csv python-basics/data/mlb_2026_hitters.csv
```

Run that command from the repository root. See [data sources](../../DATA_PROVENANCE.md) for attribution. Without the CSV, the initial Python exercises and the separate API workshop remain available.
