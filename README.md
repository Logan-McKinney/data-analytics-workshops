# Data Analytics Workshops

Hands-on Python workshops from the **University of Dayton Data Analytics Club**. Learn a repeatable workflow: ask a question, load data, inspect it, analyze it, and visualize the result. The lessons retain the original baseball, Pokémon, and Dayton weather examples and guided classroom style.

| Workshop | What you will learn | Start here |
| --- | --- | --- |
| Python basics | Variables, lists, indexing, comparisons, loops; pandas loading, inspection, selection, filtering, sorting, `groupby`; interactive Plotly bar and scatter charts | [Student notebook](python-basics/student.ipynb) · [Instructor solutions](python-basics/instructor.ipynb) |
| Working with APIs | Endpoints, GET requests, status codes, nested JSON, query parameters, JSON versus CSV, DataFrames and charts | [Student notebook](working-with-apis/student.ipynb) · [Instructor solutions](working-with-apis/instructor.ipynb) |

**Publication status:** prepared for a private GitHub repository at the owner’s request; public release and reuse licensing remain subject to review. The API instructor lesson runs offline with the included examples. The Python lesson needs an authorized local MLB CSV, which is **not redistributed** here. Original season statistics are unverified. See [data provenance](DATA_PROVENANCE.md) and [verification / remaining work](docs/VERIFICATION.md).

## Getting started

Follow the [Windows, VS Code, and Jupyter setup guide](docs/SETUP.md). It explains how to create a virtual environment, install [requirements.txt](requirements.txt), select the matching kernel, and run notebooks in order.

For a complete walkthrough, open an `instructor.ipynb`, restart the kernel, and run all cells from the top. Student notebooks intentionally contain incomplete exercises; fill these in during the workshop before running dependent cells. Solutions are public in this repository, so instructors should share the student notebook window during class.

No secret API keys or accounts are needed for the supplied offline examples. The API notebook defaults to `OFFLINE_MODE = True`. To practice live requests, change it to `False` and restart/run from the top. Network or HTTP failures are intentionally visible: switch back to offline mode and restart/run all to recover. The supplied weather is illustrative classroom data, **not a live or historical forecast**. Offline files stay fixed when names or coordinates change.

## Workshop organization

```text
data-analytics-workshops/
├── python-basics/
│   ├── student.ipynb
│   ├── instructor.ipynb
│   ├── data/README.md           # How to supply the withheld MLB CSV
│   ├── cheat-sheet.md
│   ├── instructor-key.md
│   └── instructor-guide.md
├── working-with-apis/
│   ├── student.ipynb
│   ├── instructor.ipynb
│   ├── data/                   # Original JSON and CSV fallback examples
│   ├── cheat-sheet.md
│   ├── instructor-key.md
│   └── instructor-guide.md
├── docs/SETUP.md
├── docs/VERIFICATION.md
├── scripts/verify_notebooks.py
├── requirements.txt
├── DATA_PROVENANCE.md
├── THIRD_PARTY_NOTICES.md
├── LICENSE_STATUS.md
└── CHANGELOG.md
```

The Python workshop follows a roughly 50-minute teaching plan. The API workshop also targets about 50 minutes of instructional content and can be attended without the first session. The original mini challenges are preserved; no extra exercises or datasets have been invented.

## Technologies and references

Python, pandas, Plotly Express, requests, JupyterLab, and VS Code's Python/Jupyter extensions. JSON, CSV, dictionaries, lists, and HTTP GET are the core data and API concepts.

- [PokéAPI documentation](https://pokeapi.co/docs/v2) — the original Pokémon examples.
- [Open-Meteo documentation](https://open-meteo.com/en/docs) — the original weather examples; [service terms](https://open-meteo.com/en/terms) apply to live use.
- [Cheat sheet: pandas and Plotly](python-basics/cheat-sheet.md).
- [Cheat sheet: APIs](working-with-apis/cheat-sheet.md).

## Maintenance and publication

Run `python scripts/verify_notebooks.py` for offline validation of the API instructor notebook, all notebook schemas and Python syntax, and publication hygiene. See the verification guide for checking the Python lesson with an authorized CSV. Student templates are not expected to execute unchanged.

Before committing notebooks, restart the kernel and clear all outputs, then save. Keep credentials, local data, environments, caches, and generated exports out of version control. Resolve the [licensing decisions](LICENSE_STATUS.md) before presenting this as an openly licensed teaching resource. Changes made for this publication copy are recorded in [CHANGELOG.md](CHANGELOG.md).
