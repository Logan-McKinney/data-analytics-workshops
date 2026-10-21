# Windows setup: Python, VS Code, and Jupyter

These instructions use Windows PowerShell and a project-local environment. Verification used Python 3.13.3. Use Python 3.13 to match that environment; other Python versions have not been tested here. Initial installation requires internet access or an existing local package cache; running the installed offline lessons does not.

## 1. Install the tools and open the project

## 1. Install Python 3.13 for Windows from [python.org](https://www.python.org/downloads/windows/), including the Python launcher (`py`). Check `py -3.13 --version` in a new terminal.
2. Install [VS Code](https://code.visualstudio.com/). In Extensions, install **Python** (`ms-python.python`) and **Jupyter** (`ms-toolsai.jupyter`), both published by Microsoft.
3. Extract or copy the whole `data-analytics-workshops` folder. In VS Code use **File > Open Folder** and choose that folder. Avoid opening just one notebook from a ZIP.
4. Open **Terminal > New Terminal**. Confirm `Get-Location` is the project root: `Get-ChildItem requirements.txt` should find the requirements file.

## 2. Create one environment and install dependencies

Run these commands from the repository root:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -c "import pandas, plotly.express, requests, nbformat; print('Setup complete!')"
```

Activation is optional. The explicit interpreter path above avoids PowerShell execution-policy problems with activation scripts. It also ensures installation goes into the same environment the notebooks will use.

## 3. Select the VS Code notebook kernel

## 1. Open `working-with-apis/instructor.ipynb` for a completed first run, or `student.ipynb` to follow the live workshop.
2. Choose **Select Kernel > Python Environments** and select `.venv\Scripts\python.exe` from this project. If it is missing, use **Python: Select Interpreter** from the Command Palette and enter that interpreter path, then select the notebook kernel again.
3. Leave `OFFLINE_MODE = True` for an offline run.
4. Use **Restart Kernel**, then **Run All** in the instructor notebook. In a student notebook use **Shift+Enter** and complete each fill-in before moving on. Python student exercises raise `NotImplementedError`; API student blanks are underscore placeholders and can raise `NameError` until completed.
5. Use the instructor notebook or `instructor-key.md` when you need a worked answer.

The notebooks locate their data from either the repository root or their own workshop folder. If you launch from another working directory, restart Jupyter from the project root or the relevant workshop folder. The CSV prerequisite for Python basics is explained in [python-basics/data/README.md](../python-basics/data/README.md).

## 4. JupyterLab alternative

From the repository root:

```powershell
.\.venv\Scripts\python.exe -m jupyter lab
```

Open the localhost URL printed by Jupyter. Keep its login token private. Open the desired notebook, choose the Python kernel, and restart/run from the top. Because JupyterLab is started through the environment's interpreter, its default Python kernel should use that environment. If needed, register a named kernel:

```powershell
.\.venv\Scripts\python.exe -m ipykernel install --user --name dac-workshops --display-name "DAC workshops (.venv)"
```

Then choose **DAC workshops (.venv)** in the notebook kernel selector.

## 5. Live APIs and troubleshooting

To practice actual requests, set `OFFLINE_MODE = False` in the API setup cell and restart/run the instructor notebook from the top. No key is required by these educational examples. Follow [PokéAPI fair use](https://pokeapi.co/docs/v2#fairuse) and [Open-Meteo terms](https://open-meteo.com/en/terms); do not repeatedly rerun request loops. Successful Pokémon responses are reused within a kernel session. The Open-Meteo free endpoint is intended for non-commercial use. Weather results change over time.

| Symptom | Action |
| --- | --- |
| `ModuleNotFoundError` | Select the project `.venv` kernel and rerun the install command with that interpreter. |
| `FileNotFoundError` | Check the notebook working directory and data folder. MLB data is deliberately withheld; follow its data README. |
| `NameError` | Run prior cells in order; complete student placeholders first. |
| `NotImplementedError` | This is an intentional student fill-in. Complete it or use the instructor notebook. |
| Request timeout or HTTP error | Set offline mode to `True`, restart the kernel, and run from the top. |
| Plotly chart missing | Check the selected kernel and installed packages; reopen the notebook in VS Code or JupyterLab and rerun the chart cell. |
| `py` not found | Reopen the terminal after installing Python, or use the full path to the installed Python executable to create the environment. |

The cheat sheet's optional Excel export example needs `openpyxl` if you choose to use it; Excel export is not part of the notebooks and is not included in the workshop requirements.

## Verification commands

```powershell
.\.venv\Scripts\python.exe scripts\verify_notebooks.py
```

For Python basics, supply a local CSV you are permitted to use (without adding it to Git):

```powershell
.\.venv\Scripts\python.exe scripts\verify_notebooks.py --mlb-csv .\python-basics\data\mlb_2026_hitters.csv
```

The verifier executes temporary copies in fresh kernels and does not save outputs into the publication notebooks. It also checks student templates after substituting the existing instructor solution cells in memory; that is a dependency check, not a claim that unfinished student notebooks run unchanged.
