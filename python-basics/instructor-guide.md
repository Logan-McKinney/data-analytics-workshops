# DAC Intro to Python Workshop - Instructor Itinerary

Adapted from the original workshop handout. Use [shared setup](../docs/SETUP.md) and the current notebooks for paths and environment commands.

The original MLB CSV is withheld pending redistribution permission; its season statistics are unverified. See [data instructions](data/README.md).

Target teaching time: 50 minutes | Student coding throughout | Dataset: original selected MLB teaching sample (statistics unverified)

## Main outcome

Students can open a CSV with pandas, inspect it, filter/sort it, summarize groups, and build an interactive Plotly chart.

## 0:00-0:04  Set the frame

Explain that Python is a tool for answering questions with data, not something they need to memorize. Have everyone open the notebook and run the import cell. Mention Shift+Enter and that cells build on earlier variables and should be run from top to bottom.

Instructor note: Do not spend time re-explaining installation. Fix only quick kernel/import issues; pair stuck students with a neighbor if needed.

## 0:04-0:11  Python essentials

Use the prewritten cells for variables, strings/numbers, lists, indexing, comparisons, and one simple loop. Ask students to fill in `stats[0]`. Emphasize that pandas syntax will reuse brackets, comparisons, and variable names.

Instructor note: Keep this moving. The goal is reading Python, not a programming-language survey.

## 0:11-0:17  Load + inspect the data

Students complete `pd.read_csv(...)`, then run `head()`, `shape`, and `columns`. Briefly explain DataFrame = table and Series = one column. Point out that the file has 50 rows and 20 columns.

Instructor note: Important context: the source describes a selected set of 25 players per league; this is not every MLB hitter, and the claimed rankings have not been verified. This is a good place to mention that the definition of a dataset changes what conclusions are valid.

## 0:17-0:27  Select + filter

Select a handful of useful columns. Run the 30+ HR example, then have students build `OPS > .900` and the NL + 25 HR two-condition filter. Explain `&`, parentheses, and that each condition creates True/False values.

Instructor note: If the room is slower, skip the second filter rather than rushing the charts.

## 0:27-0:34  Sort + leaders

Use `sort_values()` and `nlargest()`. Ask a quick question before running each cell: “Who do you expect near the top?” Then compare expectation to output.

Instructor note: This is where pandas starts to feel immediately useful; let students inspect names/results for a minute.

## 0:34-0:40  Group + summarize

Run league summary with `groupby()` and mean. Have students complete average OPS by position. Explain split -> calculate -> combine in plain English. Reinforce that these are averages within our selected sample.

Instructor note: Avoid overexplaining groupby internals. One clean example is enough.

## 0:40-0:47  Plotly payoff

Build the top-10 HR bar chart first. Then, if pace is good, build the OBP-vs-SLG scatter with color by league, bubble size by HR, and hover names. Let everyone hover and zoom for 30-60 seconds.

Instructor note: If time is tight, do the scatter plot only; it demonstrates interactivity better.

## 0:47-0:50  Mini challenge + close

Give students one challenge: top 10 RBI bar chart OR find 20-HR/20-SB players. Tell them the cheat sheet has the patterns. Close by restating the workflow: load -> inspect -> filter/sort -> summarize -> visualize.

Instructor note: Do not solve immediately. After ~2 minutes, show one solution from the instructor notebook and encourage them to keep experimenting after the meeting.

## Backup / troubleshooting notes

- Kernel prompt: click Select Kernel -> Python Environments -> choose the project .venv interpreter.

- ModuleNotFoundError: open the VS Code terminal and run `.\.venv\Scripts\python.exe -m pip install -r requirements.txt` on Windows or the `python3 -m pip ...` version on Mac.

- FileNotFoundError: confirm the authorized CSV is in `python-basics/data/`.

- NameError: the cell that creates that variable probably has not been run yet. Run cells from top to bottom.

- If Plotly does not render inline, rerun the cell once; if needed, use the chart in the instructor notebook as the demo while students continue the pandas portion.

## Optional discussion prompts if you are ahead

- Why might OPS tell a different story than batting average?

- What does the OBP-vs-SLG scatter show that a top-10 list does not?

- What conclusions would be unsafe because our dataset is a selected teaching sample?

- What other sports or campus data could you analyze with the exact same workflow?
