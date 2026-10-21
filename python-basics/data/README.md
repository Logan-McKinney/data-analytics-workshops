# MLB teaching data: local use only pending permission

`mlb_2026_hitters.csv` is intentionally absent from this publication copy. The original notebook attributes it to MLB.com home-run leader pages on September 22, 2026, but the source package contains no data license or redistribution permission. The original file contains 50 rows and 20 columns, with 25 records labeled AL and 25 labeled NL. These file counts were checked; the season values, collection date, and selection were not independently verified.

If you already have an authorized copy for your local teaching use, place it here under its original name. Do not commit it or its generated tables/charts until redistribution rights are established. The repository `.gitignore` excludes CSV/JSON files in this folder. No automated download or scraping is provided.

Expected columns, preserving the original file's schema:

```text
Player,Team,League,Position,G,AB,R,H,2B,3B,HR,RBI,BB,SO,SB,CS,AVG,OBP,SLG,OPS
```

The lesson uses `Player`, `Team`, `League`, `Position`, `HR`, `RBI`, `SB`, `AVG`, `OBP`, `SLG`, and `OPS`. Counting stats and rate stats should be numeric. An authorized alternative with this schema may work, but its provenance, units, and interpretation must be documented before use. No alternative data is supplied or invented here.

See [provenance and rights decisions](../../DATA_PROVENANCE.md). Until an appropriately licensed dataset is available, a fresh public checkout can read the full Python lesson and run its initial Python examples, but cannot execute the data analysis sections.
