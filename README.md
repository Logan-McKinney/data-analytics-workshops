# Data Analytics Workshops

Hands-on Python workshops I helped organize, develop, and lead through the **University of Dayton Data Analytics Club**. The lessons introduce a practical workflow: ask a question, load data, explore it with pandas, and explain the results with interactive Plotly charts.

## The workshops

| Workshop | What participants practice | Notebooks |
| --- | --- | --- |
| Python basics | Variables, lists, loops, filtering, sorting, and grouping; comparing baseball hitting statistics with bar and scatter charts | [Student exercises](python-basics/student.ipynb) · [Instructor solutions](python-basics/instructor.ipynb) |
| Working with APIs | HTTP GET requests, nested JSON, query parameters, and JSON/CSV data; exploring Pokémon attributes and plotting Dayton weather examples | [Student exercises](working-with-apis/student.ipynb) · [Instructor solutions](working-with-apis/instructor.ipynb) |

Each workshop has a roughly 50-minute teaching plan, an instructor guide, an answer key, and a cheat sheet. The API session can be used independently of the Python basics session.

## Get started

Uses Python, pandas, Plotly Express, requests, and Jupyter. From the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m jupyter lab
```

Open an `instructor.ipynb` for a complete walkthrough, or a `student.ipynb` to work through the exercises. Select the project environment as the kernel and run cells in order. Student notebooks contain intentional blanks that must be completed before dependent cells run. See the [VS Code and Jupyter setup guide](docs/SETUP.md) for more detail.

**Python lesson data:** the original MLB CSV is excluded because redistribution permission was not established. To run its data-analysis sections, place an authorized local copy at `python-basics/data/mlb_2026_hitters.csv`; the [data note](python-basics/data/README.md) lists the expected columns. Initial Python exercises do not need it.

The API notebooks default to `OFFLINE_MODE = True` and include Pokémon and weather examples. The supplied weather values are illustrative classroom data, not a live or historical forecast. Set offline mode to `False` and restart/run from the top to practice live requests to [PokéAPI](https://pokeapi.co/docs/v2) and [Open-Meteo](https://open-meteo.com/en/docs).

## Teaching resources and checks

- [Python/pandas/Plotly cheat sheet](python-basics/cheat-sheet.md) and [instructor guide](python-basics/instructor-guide.md).
- [API cheat sheet](working-with-apis/cheat-sheet.md) and [instructor guide](working-with-apis/instructor-guide.md).
- Run `python scripts/verify_notebooks.py` to check notebook structure, syntax, local links, fallback data, and API notebook execution with network calls blocked. Python data execution is skipped unless an authorized CSV is supplied with `--mlb-csv PATH`.

## Credits and data sources

Developed for the University of Dayton Data Analytics Club, with Logan McKinney helping organize, develop, and lead the workshops. The teaching materials retain the club workshop examples and shared classroom format.

Pokémon examples credit PokéAPI and its contributors; live weather examples credit Open-Meteo. See [data sources](DATA_PROVENANCE.md) and [third-party notices](THIRD_PARTY_NOTICES.md) for attribution. A repository-wide reuse license has not been selected; third-party notices still apply.
