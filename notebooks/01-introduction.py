# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "marimo>=0.23.6",
    # "dlt>=1.26.0",
    # "duckdb>=1.5.2",
    # "openhound>=0.1.4",
    # "polars>=1.40.1",
    # "pyarrow>=24.0.0",
    # "pydantic>=2.13.3",
# ]
# ///
import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import requests

    return mo, pl, requests


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Section 01: Collection basics
    ## What is OpenHound

    OpenHound is a standardized OpenGraph collector/converter and is built on top of the dlt (data load tool) library, an open source Python framework for data extraction, transformation, and loading. The dlt library already solves a lot of the issues faced when building a custom data collector.

    - **Schema validation**: Automatically catch potential data formatting issues from your source and before exporting your graph;
    - **Incremental loading**: Only process what has changed since your last run;
    - **Pre-built connectors**: Already contains pre-built connectors and an easy to use (generic) HTTP connector which deals with pagination automatically;
    - **Multi-threading**: Parallelize resource collection;

    OpenHound simplifies the use of DLT for OpenGraph collection and conversion by exposing each phase as a dedicated CLI command. During this workshop we will build an OpenHound collector using the public PokeAPI as the data source.

    ```text
    PokeAPI -> Raw data -> Pydantic models -> OpenGraph Output
    ```

    This workshop is inspired by https://github.com/dlt-hub/dlthub-education.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Learning Goals

    Before we start using OpenHound and DLT, let's try to collect data the manual way.

    By the end of this section you should be able to:

    - Get an initial list of pokemon names using the requests library;
    - Implement pagination the manual way;
    - Collect pokemon details;
    - Realize that this can be simplified.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Collecting Pokemon
    Let's start by performing manual Pokemon collection using the requests library. We'll limit the amount of Pokemon to 100. Try running the cells below and inspect the output.
    """)
    return


@app.cell
def cell_list_pokemon(requests):
    POKEMON_PAGE_URL = "https://pokeapi.co/api/v2/pokemon"

    def list_pokemon(url: str) -> dict:
        request = requests.get(
            url,
            params={"limit": 100, "offset": 0},
            headers={"User-Agent": "openhound-workshop/0.1"},
        )
        return request.json()

    pokemon_page = list_pokemon(POKEMON_PAGE_URL)
    return POKEMON_PAGE_URL, pokemon_page


@app.cell
def _(pokemon_page):
    pokemon_page
    return


@app.cell
def _(mo, pokemon_page):
    mo.md(f"""
    ## Response summary
    If everything works correctly you should see the API response in the cell above. The response contains these top-level fields:

    | Field | Value | Description |
    |---|---|---|
    | `count` | `{pokemon_page["count"]}` | The total amount of Pokemon in the DB|
    | `next` | `{pokemon_page["next"]}` | The URL to fetch the next page |
    | `previous` | `{pokemon_page["previous"]}` | The previous page, which is None since this is our first request|
    | `results` | `{len(pokemon_page["results"])}` records in this page | The amount of records in the current request|


    As you may have noticed, the list of results only contains a Pokemon name and a URL. We'll want to fetch the Pokemon details later as well.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Marimo tricks
    Did you know you can render the response as an interactive Marimo table? Check this out!
    """)
    return


@app.cell(hide_code=True)
def _(pl, pokemon_page):
    pl.DataFrame(pokemon_page["results"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 1

    Marimo cells are reactive, meaning that when a value or variable changes in one cell, all cells that depend on it are automatically updated.

    Try changing the following parameters and see what happens when you run the cell again:

    - Change `limit=10` to `limit=100`.
    - Change `offset=0` to `offset=100`.
    - Observe how `next`, `previous`, and `results` change.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Pagination

    PokeAPI uses an offset in order to paginate results. You will have to use the following parameters in order to collect all Pokemon.

    | Field or parameter | Meaning |
    |---|---|
    | `limit` | Number of records requested in the page. |
    | `offset` | Starting position for the page. |
    | `next` | Full URL for the next page, or `null` at the end. |
    | `previous` | Full URL for the previous page, or `null` at the beginning. |

    Example pages:

    - First page: `https://pokeapi.co/api/v2/pokemon?limit=10&offset=0`
    - Second page: `https://pokeapi.co/api/v2/pokemon?limit=10&offset=10`
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 2
    Try to collect all Pokemon by creating the paginate_pokemon function. Here is a modified example to get started, fill in the "TODO" placeholders based on the pagination description mentioned previously.
    """)
    return


@app.cell
def _(requests):
    def paginate_pokemon(url: str) -> list[dict]:
        pokemon = []
        next_url = url

        while next_url:
            response = requests.get(
                next_url,
                headers={"User-Agent": "openhound-workshop/0.1"},
            )
            page = response.json()
            pokemon.extend(
                page["TODO"]
            )  # Replace TODO with the field containing the list of Pokemon
            next_url = page[
                "TODO"
            ]  # Replace TODO with the field containing the next page
        return pokemon

    return (paginate_pokemon,)


@app.cell
def _(POKEMON_PAGE_URL, paginate_pokemon):
    all_pokemon = paginate_pokemon(POKEMON_PAGE_URL)
    return (all_pokemon,)


@app.cell(hide_code=True)
def _(all_pokemon, pl):
    pl.DataFrame(all_pokemon)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 3
    We have successfully collected all Pokemon but are still missing the Pokemon details. Finalize the `collect_pokemon_details` function to collect the Pokemon details.
    """)
    return


@app.cell
def _(requests):
    def collect_pokemon_details(pokemon: list) -> list[dict]:
        pokemon_details = []
        for poke in pokemon:
            # Replace TODO with the field containing the URL for the Pokemon details
            response = requests.get(poke["TODO"]).json()
            pokemon_details.append(response)
        return pokemon_details

    return (collect_pokemon_details,)


@app.cell
def _(all_pokemon, collect_pokemon_details):
    pokemon_details = collect_pokemon_details(all_pokemon[:2])
    return (pokemon_details,)


@app.cell
def _(pl, pokemon_details):
    pl.DataFrame(pokemon_details)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Wrapping up

    Pagination works differently across APIs and you may have noticed that collecting all Pokemon details may take some time; we need to perform an additional request for each of the 1000+ Pokemon. Instead of developing custom clients or collectors for every API, DLT provides a built-in RESTClient that automatically handles pagination, rate limiting and parallelization.

    Before we re-implement our Pokemon collector, let’s first take a look at data validation. After this introduction, the workshop will continue with the basics of Pydantic to validate API responses.
    """)
    return


if __name__ == "__main__":
    app.run()
