# Python + pandas Quick Reference

Adapted from the original workshop handout. Use [shared setup](../docs/SETUP.md) and the current notebooks for paths and environment commands.

The original MLB CSV is withheld pending redistribution permission; its season statistics are unverified. See [data instructions](data/README.md).

Use these patterns to answer your own questions; change columns to fit the dataset.

## Python essentials

```python
name = "Pete Alonso"             # variable
hr = 40                          # number
stats = ["HR", "RBI", "OPS"]     # list
stats[0]                         # first item
print(name)                      # show a value
hr >= 30                         # comparison -> True/False
team == "BAL"                    # compare text (after defining team)
for stat in stats:
    print(stat)                  # repeat for each item
```

## Load and inspect

```python
import pandas as pd
import plotly.express as px

# DATA_DIR is defined in the notebook setup cell.
df = pd.read_csv(DATA_DIR / "mlb_2026_hitters.csv")
```

| Pattern | Purpose |
| --- | --- |
| `df.head()` / `df.tail()` | First / last five rows |
| `df.shape` | Rows and columns |
| `df.columns` | Column names |
| `df.info()` | Types and missing values |
| `df.describe()` | Numeric summary |
| `df["HR"]` | One column |
| `df[["Player", "HR", "OPS"]]` | Multiple columns |

## Filter, sort, summarize

```python
df[df["HR"] >= 30]                              # one condition
df[df["Team"] == "CHC"]                         # text condition
df[(df["HR"] >= 25) & (df["SB"] >= 20)]          # AND
df[(df["League"] == "AL") | (df["OPS"] > .900)]  # OR

df.sort_values("HR", ascending=False)  # largest first
df.nlargest(10, "OPS")                 # top 10 OPS
df.nsmallest(5, "SO")                  # fewest strikeouts
df["HR"].mean()
df["HR"].median()
df["HR"].max()
df["Team"].value_counts()
df.groupby("League")["OPS"].mean()
df.groupby("Position")[["HR", "OPS"]].mean().round(3)
df.loc[0, "Player"]                    # row label + column
df.iloc[0]                            # first row by position
```

## Plotly patterns

```python
top10 = df.nlargest(10, "HR")
fig = px.bar(
    top10,
    x="Player",
    y="HR",
    title="Top Home Run Hitters"
)
fig.show()

fig = px.scatter(
    df,
    x="OBP",
    y="SLG",
    color="League",
    size="HR",
    hover_name="Player"
)
fig.show()
```

Common options: `color="League"`, `size="HR"`, `hover_name="Player"`, `hover_data=["Team", "OPS"]`, `orientation="h"`, and `title="My Chart"`.

## Everyday pandas patterns

```python
df.isna().sum()                          # count missing values
df.dropna()                              # drop rows with missing data
df["col"].fillna(0)                      # replace missing values in a column
df["K_rate"] = df["SO"] / df["AB"]
df["OPS_plus_100"] = df["OPS"] * 100
df.rename(columns={"HR": "HomeRuns"})
df["Team"] = df["Team"].str.strip()
df.to_csv("results.csv", index=False)
df.to_excel("results.xlsx", index=False)  # optional: requires openpyxl
```

`col` is a pattern placeholder for a real column name. Excel export is optional and is not used in the notebooks. Results from the withheld MLB data must remain local until redistribution rights are cleared.

## When something breaks

- Read the last line of the error first.
- Check spelling and capitalization of column names; use `df.columns`.
- Run earlier cells again: variables only exist after their cells run.
- Put the authorized CSV in `python-basics/data/`.
- Use Shift+Enter to run a notebook cell. Documentation is part of normal programming.

## MLB stat reminders

| Stat | Meaning |
| --- | --- |
| AVG | Batting average |
| OBP | On-base percentage |
| SLG | Slugging percentage |
| OPS | OBP + SLG |
| HR | Home runs |
| RBI | Runs batted in |
| SB | Stolen bases |
| SO | Strikeouts |

Best habit: start with a question, then choose the pandas operation that answers it.
