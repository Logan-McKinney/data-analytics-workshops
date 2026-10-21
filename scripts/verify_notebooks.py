"""Validate publication notebooks and execute temporary copies without network calls.

Usage: python scripts/verify_notebooks.py [--mlb-csv PATH]
No packages are installed and no execution outputs are written to the repository.
"""
from pathlib import Path
import argparse
import ast
import copy
import json
import re
import shutil
import tempfile

import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
SECTIONS = ("python-basics", "working-with-apis")


def validate_static():
    count = 0
    for path in sorted(ROOT.glob("*/*.ipynb")):
        nb = nbformat.read(path, as_version=4)
        nbformat.validate(nb)
        for index, cell in enumerate(nb.cells):
            if cell.cell_type != "code":
                continue
            ast.parse(cell.source, filename=f"{path.name}:cell-{index}")
            assert cell.execution_count is None and not cell.outputs, path
            if path.name == "instructor.ipynb":
                assert not re.search(r"\bTODO\b|_{8,}", cell.source), (path, index)
            count += 1
    for path in (ROOT / "scripts").glob("*.py"):
        ast.parse(path.read_text(encoding="utf-8"), filename=path.name)
    data = ROOT / "working-with-apis" / "data"
    import pandas as pd
    weather = json.loads((data / "weather_offline_example.json").read_text(encoding="utf-8"))
    csv = pd.read_csv(data / "weather_offline_example.csv")
    assert len(csv) == len(weather["hourly"]["time"]) == 72
    assert csv["time"].tolist() == weather["hourly"]["time"]
    assert csv["temperature_2m_F"].tolist() == weather["hourly"]["temperature_2m"]
    assert csv["precipitation_probability_pct"].tolist() == weather["hourly"]["precipitation_probability"]
    pokemon = json.loads((data / "pokemon_table_fallback.json").read_text(encoding="utf-8"))
    assert len(pokemon) == 12
    # Follow relative Markdown links without contacting external sites.
    for path in ROOT.rglob("*.md"):
        for link in re.findall(r"(?<!!)\[[^\]]*\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            if "://" not in link and not link.startswith("#"):
                assert (path.parent / link.split("#")[0]).exists(), (path, link)
    print(f"PASS: four notebook schemas, {count} code-cell syntax checks, clean outputs, instructor completeness, local Markdown links, 12 Pokémon rows, 72 matching weather rows.")


GUARD = '''import requests
def _deny_request(*args, **kwargs):
    raise AssertionError("Verification forbids network requests")
requests.sessions.Session.request = _deny_request
'''

ASSERTIONS = {
    "python-basics": '''assert df.shape == (50, 20)
assert df["League"].value_counts().to_dict() == {"AL": 25, "NL": 25}
assert df.sort_values("HR", ascending=False)["HR"].is_monotonic_decreasing
assert len(df.nlargest(10, "OPS")) == 10
assert {"HR", "SB", "OPS"}.issubset(power_speed.columns)
assert len(fig.data) > 0
''',
    "working-with-apis": '''assert OFFLINE_MODE is True
assert pokemon["name"] == "pikachu"
assert pokemon_df.shape == (12, 11)
assert weather_df.shape == (72, 3)
assert weather_csv_df.shape == (72, 3)
assert weather_df["temperature_f"].tolist() == weather_csv_df["temperature_2m_F"].tolist()
assert "Illustrative Offline" in fig.layout.title.text
assert len(fig.data) > 0
''',
}


def execute(section, workdir, student=False):
    instructor = nbformat.read(ROOT / section / "instructor.ipynb", as_version=4)
    nb = nbformat.read(ROOT / section / ("student.ipynb" if student else "instructor.ipynb"), as_version=4)
    if student:
        assert len(nb.cells) == len(instructor.cells)
        for i, cell in enumerate(nb.cells):
            if "exercise" in cell.metadata.get("tags", []):
                nb.cells[i] = copy.deepcopy(instructor.cells[i])
    nb.cells.insert(0, nbformat.v4.new_code_cell(GUARD))
    nb.cells.append(nbformat.v4.new_code_cell(ASSERTIONS[section]))
    client = NotebookClient(nb, timeout=90, kernel_name="python3", allow_errors=False,
                            resources={"metadata": {"path": str(workdir)}})
    client.execute()
    figures = sum("application/vnd.plotly.v1+json" in output.get("data", {})
                  for cell in nb.cells if cell.cell_type == "code" for output in cell.outputs)
    assert figures == 2, (section, figures)
    label = "student with instructor fill-ins substituted in memory" if student else "instructor"
    print(f"PASS: {section}/{label}; fresh kernel, two Plotly figures, data assertions, network guard.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--mlb-csv", type=Path, help="authorized original 50-row, 20-column teaching CSV for local checking")
    args = parser.parse_args()
    validate_static()
    with tempfile.TemporaryDirectory(prefix="dac-verify-") as temporary:
        workdir = Path(temporary)
        for section in SECTIONS:
            shutil.copytree(ROOT / section, workdir / section)
        if args.mlb_csv:
            shutil.copyfile(args.mlb_csv.resolve(), workdir / "python-basics" / "data" / "mlb_2026_hitters.csv")
        for section in SECTIONS:
            if section == "python-basics" and not args.mlb_csv:
                print("SKIP: Python data execution; original CSV withheld pending redistribution permission. Use --mlb-csv for an authorized local check.")
                continue
            execute(section, workdir)
            execute(section, workdir / section, student=True)


if __name__ == "__main__":
    main()
