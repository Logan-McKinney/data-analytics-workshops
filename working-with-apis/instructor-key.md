# Instructor Fill-In Key

Adapted from the original workshop handout. Use [shared setup](../docs/SETUP.md) and the current notebooks for paths and environment commands.

`OFFLINE_MODE = True` is the default. Original live-request fill-ins remain for teaching; instructor.ipynb contains the completed code.

Keep this beside you while screen-sharing student.ipynb

## TODO 1 - Send first GET request

```python
response = requests.get(url, timeout=10)
```

requests.get() sends an HTTP GET request. timeout prevents a bad network call from hanging forever.

## TODO 2 - Status code

```python
print(response.status_code)
```

Expect 200 when the request works.

## TODO 3 - Stop on HTTP error

```python
response.raise_for_status()
```

This turns HTTP errors such as 404 into a visible Python exception.

## TODO 4 - JSON to Python

```python
pokemon = response.json()
```

JSON objects become Python dictionaries/lists.

## TODO 5 - Nested values

```python
name = pokemon["name"]
height_m = pokemon["height"] / 10
weight_kg = pokemon["weight"] / 10
primary_type = pokemon["types"][0]["type"]["name"]
attack = pokemon["stats"][1]["base_stat"]
```

Walk left-to-right through keys/list indices. The important skill is reading the response structure.

## TODO 6 - Endpoint inside loop

```python
r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}", timeout=10)
```

Same endpoint pattern, different resource name each pass.

## TODO 7 - Create DataFrame

```python
pokemon_df = pd.DataFrame(rows)
```

Each dictionary becomes one row; dictionary keys become columns.

## TODO 8 - Sort

```python
pokemon_df.sort_values("attack", ascending=False).head(5)
```

Fast reminder of pandas; do not dwell here.

## TODO 9 - Scatter plot

```python
x="attack",
y="defense",
```

The rest of the Plotly call is already provided.

## TODO 10 - Weather variables

```python
"hourly": "temperature_2m,precipitation_probability",
```

Open-Meteo lets multiple requested variables be comma-separated.

## TODO 11 - Weather GET with params

```python
weather_response = requests.get(weather_url, params=params, timeout=10)
```

requests builds the query string from the params dictionary.

## TODO 12 - Weather DataFrame

```python
"time": weather["hourly"]["time"],
"temperature_f": weather["hourly"]["temperature_2m"],
"precip_probability": weather["hourly"]["precipitation_probability"],
```

Three equal-length arrays become three DataFrame columns.

## TODO 13 - Weather line chart

```python
x="time",
y="temperature_f",
```

The datetime conversion above makes the x-axis behave as time.

## TODO 14 - Request CSV

```python
csv_params["format"] = "csv"
```

Same endpoint and parameters; only response format changes.

## Emergency fallback

At any point, set:

```python
OFFLINE_MODE = True
```

Then restart the kernel and run from the top (completing student blanks first). Pokémon fallbacks retain the supplied teaching values; the weather fallback is clearly labeled illustrative classroom data and is only there to keep the workflow moving if the live API/network fails.
