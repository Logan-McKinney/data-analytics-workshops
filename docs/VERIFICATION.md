# Verification and remaining work

Prepared October 21, 2026. Checks used the existing Python 3.13.3 installation on Windows 11 and the direct package versions in requirements.txt. No dependencies were installed and no live API requests were made. Provider documentation was consulted online only to review licensing, attribution, and service terms.

## Results

| Check | Result |
| --- | --- |
| Original file preservation | SHA-256 comparison of all 27 original files: unchanged. |
| Notebook schema and syntax | All four notebooks validate; all 68 code cells parse as Python. The verification script also parses. |
| Publication hygiene | No saved outputs or execution counts; completed instructor notebooks contain no TODOs or underscore blanks. No absolute local paths or machine-specific notebook metadata retained. |
| Local document references | Relative Markdown file links resolve. |
| API fallback consistency | 12 Pokémon table records; 72 matching weather timestamps, temperature values, and precipitation values across JSON and CSV. All four fallback files are byte-for-byte identical to the originals. |
| Python instructor execution | Passed in a fresh kernel using a temporary copy of the original CSV; data assertions and both Plotly figures passed. Original CSV was read locally, not added to the publication tree. |
| API instructor execution | Passed in a fresh kernel with default offline mode; expected tables and both Plotly figures passed; the optional 404 demo was skipped. |
| Student dependency checks | Both passed after substituting the existing instructor exercise solutions in memory. Instructor checks ran from a temporary project root; student checks ran from each workshop folder, exercising both supported working directories. |
| Network exclusion | All four execution runs patched requests' HTTP entry point to raise if called. No request was attempted. |
| Privacy / secret scan | All proposed public files scanned for common API tokens, private keys, credential assignments, email addresses, absolute home paths, private-network addresses, and the removed meeting/signature details: no matches after review. Notebook sources were decoded before scanning to avoid JSON escape false positives. |

The source DOCX text and all seven PDF counterparts were extracted for inspection. Duplicate Office/PDF exports were excluded to avoid stale commands, paths, and document metadata. The dated meeting email, named signature, and room/time details were not copied. Public notebook metadata is restricted to language/kernel information and exercise tags; saved output payloads were removed. A private source inventory and scan manifest with hashes remain outside the proposed public folder, in the sibling `workshop-publication-review` folder.

The first execution attempt was blocked by Windows sandbox temporary-directory permissions. The approved run outside the sandbox completed with exit code 0. Windows ZeroMQ emitted an event-loop warning and a transient connection-reset message during kernel shutdown; all four execution checks still completed successfully. These runtime diagnostics are not notebook lesson errors.

This is a targeted local scan, not a guarantee that every possible secret format can be detected. The public tree contains only Markdown, Python, notebook JSON, the four supplied fallback files, requirements.txt, and .gitignore; no original Office/PDF metadata, generated figures, local CSV, environments, or live caches are included.

## Reproduce checks

Run `python scripts/verify_notebooks.py` from the repository root with the dependencies installed. This checks notebook schemas, Python syntax, clean publication outputs, relative Markdown links, API fallback consistency, and execution in fresh kernels with HTTP calls blocked.

Use `--mlb-csv PATH` to check the original Python lesson locally with an authorized original teaching CSV. The script copies that data into a temporary directory, never into the publication tree. It also checks student dependencies by substituting the existing instructor solutions for tagged exercise cells in temporary in-memory copies. Unfinished student templates intentionally do not run unchanged.

## Remaining attention before publication

- Resolve redistribution permission for the MLB CSV or obtain a suitable licensed source with a documented provenance trail. The original remains outside this project; Python data analysis cannot run from a fresh public checkout until the reader supplies an authorized local copy.
- Confirm the MLB file's claimed season values, source date, and selection. Only its shape, labels, and lesson behavior have been checked.
- Select a license for original code, prose, and illustrative data. No new license is imposed in this preparation.
- The Pokémon fallback extraction date and exact collection history are unavailable. They retain the source attribution and upstream repository license notice; current API values were not audited.
- Live API availability, actual HTTP statuses, current response schemas, and Open-Meteo CSV preamble parsing are not execution-tested. Offline execution does not prove these live paths. Classroom internet checks are still needed before using live mode.
- VS Code interaction, JupyterLab browser rendering, and Plotly hover/zoom behavior require a manual user-interface check. Automated checks verify successful figure generation and figure data, not a human's screen.
- A clean installation from requirements.txt was not attempted; checks use already installed packages. Direct dependency versions are pinned, but transitive dependencies are not locked. No large dependencies were installed.

The source Word/PDF exports and dated email are deliberately excluded from the public tree. Useful handouts are adapted as Markdown. The notebooks and shared setup guide are authoritative for environment commands and data paths.
