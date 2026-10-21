# API + Python Quick Reference

Adapted from the original workshop handout. Use [shared setup](../docs/SETUP.md) and the current notebooks for paths and environment commands.

`OFFLINE_MODE = True` is the default. Original live-request fill-ins remain for teaching; instructor.ipynb contains the completed code.

Data Analytics Club - Workshop 2

## The API workflow

`endpoint -> GET request -> response -> JSON / CSV -> DataFrame`

Think: Where do I ask? → What do I send? → Did it work? → What came back? → How do I analyze it?

## Making a request

```python
import requests

response = requests.get(url, timeout=10)
print(response.status_code)
response.raise_for_status()
data = response.json()
```

## Query parameters

```python
params = {
    "latitude": 39.7589,
    "longitude": -84.1916,
    "forecast_days": 3
}
response = requests.get(url, params=params, timeout=10)
```

Using a params dictionary is cleaner than manually building a long URL.

## Reading JSON in Python

| JSON / Python task | Pattern |
| --- | --- |
| Object / dictionary | `data["name"]` |
| Array / list | `data["items"][0]` |
| Nested object | `data["type"]["name"]` |
| Inspect keys | `data.keys()` |
| Inspect type | `type(data)` |

## Useful HTTP status codes

200 = success     400 = bad request     401/403 = auth/permission     404 = not found     429 = too many requests

## Before using an unfamiliar API

- Find the base endpoint in the documentation.

- Check whether an API key/login is required.

- Look for required vs. optional parameters.

- Find a sample response and identify the fields you actually need.

- Check limits, pagination, and usage rules if you are pulling lots of data.

## Turning API data into pandas

```python
df = pd.DataFrame(rows)
df.head()
df.columns
df.sort_values("attack", ascending=False)
```

For nested JSON, first create one simple dictionary per observation, then build the DataFrame from that list of dictionaries.

## A small flattening pattern

```python
row = {
    "name": data["name"],
    "height": data["height"],
    "type": data["types"][0]["type"]["name"]
}
```

## CSV responses

```python
from io import StringIO

response = requests.get(url, params=params, timeout=10)
df = pd.read_csv(StringIO(response.text))
```

Some APIs return JSON by default but can also return CSV. Always check the API documentation because formats differ.

## Quick Plotly patterns

```python
px.scatter(df, x="attack", y="defense", hover_name="name")
px.line(df, x="time", y="temperature_f")
px.bar(df, x="name", y="value")
```

## Common problems

ModuleNotFoundError

Install the missing package in the active Python environment.

JSON key error

Print data.keys() and inspect the actual nesting.

404

Check the endpoint/resource spelling.

401 / 403

The API may require authentication or permission.

Request hangs/fails

Use timeout=10; check Wi-Fi; use the workshop fallback files.

## Best habit: read the docs

PokéAPI: https://pokeapi.co/docs/v2
Open-Meteo: https://open-meteo.com/en/docs

You are not expected to memorize API syntax. Learn the repeatable workflow, then use documentation to adapt it.
