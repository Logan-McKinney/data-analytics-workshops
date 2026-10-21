# Instructor Itinerary - Python Workshop: Working with APIs

Adapted from the original workshop handout. Use [shared setup](../docs/SETUP.md) and the current notebooks for paths and environment commands.

`OFFLINE_MODE = True` is the default. Original live-request fill-ins remain for teaching; instructor.ipynb contains the completed code.

Target: about 50 minutes of instructional content, leaving ~10 minutes for club welcome, settling in, questions, and wrap-up.
## 0-4 min

What an API is

Use the endpoint → request → response → format → DataFrame mental model. Mention that students do not need to memorize APIs; documentation is part of the job.

Do not reteach variables/pandas. Give only enough context for students who missed Workshop 1.

## 4-12 min

PokéAPI: first GET request

Open the student notebook. In live mode, fill TODOs 1-4. Show the 200 status code, response.json(), type(pokemon), and pokemon.keys().

Pause on the difference between response (HTTP object) and pokemon (Python dict).

## 12-17 min

Nested JSON

Fill TODO 5. Follow dict keys and list indices to name, height, type, and attack.

This is the key conceptual moment: inspect structure instead of guessing.

## 17-25 min

Many responses → DataFrame

Briefly explain the supplied pokemon_to_row() helper, then fill TODOs 6-7. Request 12 Pokémon and create pokemon_df.

Do not spend time explaining the whole comprehension inside the helper.

## 25-30 min

Quick analysis + Plotly

Fill TODOs 8-9. Sort top attack values and make the interactive attack-vs-defense scatter plot. Hover over a few points.

Connect back to Workshop 1: same pandas/Plotly, new data source.

## 30-34 min

Transition: different API, same workflow

Open-Meteo uses query parameters rather than a Pokémon name in the endpoint. Show the docs briefly if useful.

Emphasize that API design varies, but requests.get + response inspection stays familiar.

## 34-42 min

Open-Meteo JSON → DataFrame

Fill TODOs 10-12. Show params, send request, inspect weather["hourly"], then build weather_df and parse time.

Point out parallel arrays: time[i], temperature[i], precipitation[i] describe the same hour.

## 42-46 min

Weather Plotly chart

Fill TODO 13 and show the weather line chart, explaining whether it uses live or illustrative offline values.

Hover/zoom quickly so the class sees why interactive plots are useful.

## 46-48 min

JSON vs CSV

Fill TODO 14. Add format=csv and read the returned text. Explain that the API and the data format are separate choices.

Do not spend time on Open-Meteo CSV metadata quirks beyond skiprows=3.

## 48-50 min

Mini challenge + recap

Students change a Pokémon, chart axes, or weather coordinates. End on the five documentation questions in the notebook.

If pacing is behind, skip CSV or the challenge before cutting core JSON/API concepts.

## Presenter setup before students arrive

- Open student.ipynb and select the project .venv kernel.

- Keep instructor.ipynb open privately as a backup.

- Keep [instructor-key.md](instructor-key.md) on a second screen or print it.

- Run the environment import cell once.

- Test PokéAPI and Open-Meteo on the classroom network. Offline mode is the default; enable live mode only when demonstrating requests.

- Keep the workshop data/ folder intact so fallback files can be found.

## Pacing / cut order

If time is tight: (1) skip the optional 404 demo, (2) shorten the student challenge, (3) skip the live CSV call and explain it verbally. Do not cut the first GET request, nested JSON, params, or JSON→DataFrame workflow.
