# DATA ANALYTICS CLUB - PRESENTER FILL-IN KEY

Adapted from the original workshop handout. Use [shared setup](../docs/SETUP.md) and the current notebooks for paths and environment commands.

The original MLB CSV is withheld pending redistribution permission; its season statistics are unverified. See [data instructions](data/README.md).

Screen-share STUDENT notebook | Keep COMPLETE notebook private

## 1. List indexing

Cue: print the first item in the list using index 0

```python
print(stats[0])
```

Say: Python indexing starts at 0.

## 2. Load the CSV

Cue: load mlb_2026_hitters.csv into a DataFrame named df

```python
df = pd.read_csv(DATA_DIR / "mlb_2026_hitters.csv")
df
```

Say: A DataFrame is pandas' table object; df is just our variable name.

## 3. Preview

Cue: show the first 5 rows

```python
df.head()
```

Say: head() is a quick first look at a new dataset.

## 4. Dataset size

Cue: how many rows and columns?

```python
df.shape
```

Say: shape returns (rows, columns). Inspect df.shape; the original file has (50, 20).

## 5. Column names

Cue: list the column names

```python
df.columns
```

Say: Always inspect what fields you actually have.

## 6. Select columns

Cue: Player, Team, League, HR, AVG, OPS

```python
df[["Player", "Team", "League", "HR", "AVG", "OPS"]].head(10)
```

Say: Double brackets select multiple columns.

LIVE FILL-INS - CONTINUED

## 7. Filter: OPS > .900

Cue: save players with OPS above .900 as elite_ops

```python
elite_ops = df[df["OPS"] > .900]
elite_ops[["Player", "Team", "OPS"]].sort_values("OPS", ascending=False)
```

Say: Read it literally: rows where OPS is greater than .900.

## 8. Two-condition filter

Cue: NL players with at least 25 HR

```python
nl_power = df[(df["League"] == "NL") & (df["HR"] >= 25)]
nl_power[["Player", "Team", "HR", "OPS"]]
```

Say: Use & for AND; each condition gets parentheses.

## 9. Sort HR leaders

Cue: most HR to fewest HR

```python
df.sort_values("HR", ascending=False)[["Player", "Team", "HR"]].head(10)
```

Say: ascending=False means largest first.

## 10. Top 10 OPS

Cue: show the 10 highest OPS values

```python
df.nlargest(10, "OPS")[["Player", "Team", "OPS"]]
```

Say: nlargest is a shortcut for top-N questions.

## 11. Group by position

Cue: average OPS by position

```python
df.groupby("Position")["OPS"].mean().sort_values(ascending=False).round(3)
```

Say: groupby splits into groups, then mean() summarizes each.

## 12. Plotly bar chart

Cue: fill in x and y

```python
x="HR",
y="Player",
```

Say: Run it, then hover over bars to show interactivity.

## 13. Plotly scatter

Cue: fill in x and y

```python
x="OBP",
y="SLG",
```

Say: Bubble size = HR; hover shows player details.

## MINI-CHALLENGE BACKUP

```python
power_speed = df[(df["HR"] >= 20) & (df["SB"] >= 20)]
power_speed[["Player", "Team", "HR", "SB", "OPS"]].sort_values(["HR", "SB"], ascending=False)
```

## FAST RECOVERY

Kernel: Select Kernel -> installed Python.   File error: put an authorized CSV in the workshop data/ folder.   Package error: follow the shared setup guide using the project .venv interpreter.

Lost your place: open instructor.ipynb privately and jump to the same section heading.
