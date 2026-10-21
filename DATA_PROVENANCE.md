# Dataset provenance and redistribution review

Reviewed October 21, 2026. File inspection is separate from factual validation. No API data was fetched during execution checks. Browser access was limited to provider documentation and licensing research.

| Original asset | Evidence / meaning | Publication decision |
| --- | --- | --- |
| `mlb_2026_hitters.csv` | Notebook attributes a selected sample to MLB.com, September 22, 2026. File has 50 rows, 20 columns, 25 AL and 25 NL records. No license, collection script, exact source URLs, or permission accompanies it. | **Withheld**. Retain the original outside this project. Local execution can use an authorized copy; public execution of the complete Python lesson remains blocked by this missing data. |
| `pikachu_fallback.json` | Original trimmed PokéAPI-shaped response; its note describes Pikachu values. No retrieval timestamp. | Included unchanged, with PokéAPI attribution and BSD notice in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). |
| `pokemon_table_fallback.json` | Original flattened 12-Pokémon table used by the lesson. No retrieval timestamp or extraction script. | Included unchanged under the upstream repository's BSD-3-Clause notice; no independent audit against current API values. |
| `weather_offline_example.json` | Original file explicitly calls itself illustrative classroom data, not a live or historical forecast; 72 hourly examples for Dayton. | Included unchanged as the user-authorized existing classroom fallback. No claim that these are measured or forecast values. |
| `weather_offline_example.csv` | Same 72 illustrative records, with CSV-specific column names. | Included unchanged; cross-checked against the JSON values. |

## Provider sources and limitations

- [MLB terms](https://www.mlb.com/official-information/terms-of-use): redistribution permission is unconfirmed. The CSV stays excluded. The source notebook's claim of real 2026 statistics has been qualified rather than repeated as fact.
- [PokéAPI repository](https://github.com/PokeAPI/pokeapi) and [BSD-3-Clause license](https://github.com/PokeAPI/pokeapi/blob/master/LICENSE.md): the upstream repository publishes its license and trademark notice. The retained classroom extracts contain numeric/tabular facts and resource names, with no sprites or artwork. Their precise extraction history is unavailable; inclusion relies on that upstream license and the original attribution, not on a claim of trademark ownership or endorsement. [API documentation](https://pokeapi.co/docs/v2) describes the endpoint and fair-use policy.
- [Open-Meteo terms](https://open-meteo.com/en/terms) and [data licensing statement](https://github.com/open-meteo/open-meteo#data-license): live API data is offered under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). The notebook credits Open-Meteo beside the weather section and describes field selection, renaming, and datetime parsing. **This does not turn the supplied illustrative classroom weather into an Open-Meteo forecast.**

The classroom weather files have no separate license in the source package. Their reuse here follows the owner's instruction to preserve the existing permitted offline examples. A repository-wide reuse license still requires the owner's decision; see [LICENSE_STATUS.md](LICENSE_STATUS.md).

Before adding future data, record its source URL, retrieval date, license/permission, modifications, and attribution requirements. Do not commit live response caches or MLB outputs as a way around the withheld CSV.
