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
    # "requests>=2.34.1",
    # "polars>=1.40.1"
# ]
# ///

import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import polars as pl
    import requests
    from pydantic import AnyHttpUrl, BaseModel, ConfigDict, ValidationError

    return AnyHttpUrl, BaseModel, ConfigDict, ValidationError, mo, pl, requests


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Section 02: Pydantic Basics

    In the previous section, we collected Pokemon data manually using `requests` and parsed the responses as raw Python dictionaries. When converting this raw data into OpenGraph, we need to ensure that the collected data is consistent and valid. Saving API responses without any validation can lead to several issues:

    - A field can be missing.
    - A field can have the wrong type.
    - Typos in field names are only found at runtime.

    Pydantic lets us describe the shape of the data we expect and validate API responses before we convert resources to OpenGraph nodes and edges.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Learning Goals

    By the end of this section, you should be able to:

    - Define a Pydantic model for a simple API response
    - Parse raw dictionaries into Pydantic objects
    - Model nested API responses
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Reusing the Pokemon list

    We will start with the same `https://pokeapi.co/api/v2/pokemon` endpoint from the introduction. The Pokemon list response only contains the Pokemon name and detail URL.
    """)
    return


@app.cell
def _(requests):
    POKEMON_PAGE_URL = "https://pokeapi.co/api/v2/pokemon"

    def list_pokemons(url: str) -> dict:
        request = requests.get(
            url,
            params={"limit": 100, "offset": 0},
            headers={"User-Agent": "openhound-workshop/0.1"},
        )
        return request.json()

    pokemon_page = list_pokemons(POKEMON_PAGE_URL)
    return (pokemon_page,)


@app.cell
def _(pokemon_page):
    pokemon_page
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## A base Pokemon model

    A Pydantic model declares the fields we expect and their data type. The `https://pokeapi.co/api/v2/pokemon` endpoint returns results that look like the following:

    ```json
    {
      "name": "bulbasaur",
      "url": "https://pokeapi.co/api/v2/pokemon/1/"
    }
    ```

    We can model that with a Pydantic `BaseModel`.
    """)
    return


@app.cell
def _(AnyHttpUrl, BaseModel):
    class Pokemon(BaseModel):
        name: str
        url: AnyHttpUrl

    return (Pokemon,)


@app.cell
def _(Pokemon, pokemon_page):
    first_pokemon = pokemon_page["results"][0]
    first_pokemon_parsed = Pokemon.model_validate(first_pokemon)
    first_pokemon_parsed
    return (first_pokemon_parsed,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    `model_validate` takes a raw dictionary and returns a Pydantic object. Pydantic checked that:

    - `name` exists and is a string.
    - `url` exists and is a **valid** HTTP URL.

    If either field is missing or invalid, Pydantic raises an error.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 1: Validation Errors

    Let's fix a Pokemon record. Try fixing the `url` field and see if the validation passes.
    """)
    return


@app.cell
def _(Pokemon, ValidationError):
    not_a_url = {"name": "bulbasaur", "url": "htt//pokeapi.co/api/v2/pokemon/1/"}
    try:
        Pokemon.model_validate(not_a_url)
    except ValidationError as e:
        print(e)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    By adding Pydantic validators, bad or unexpected data fails early during the collection pipeline instead of failing later during the graph conversion, which may lead to unexpected output in the graph.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 2: Modeling The Full Page

    The full API response has pagination metadata and a nested list of Pokemon records. Pydantic validates nested models automatically. Try completing the full PokemonPage model below. We added a Pydantic config to fail validation if you missed any fields from the API response, so make sure all the fields are defined!
    """)
    return


@app.cell
def _(BaseModel, ConfigDict, Pokemon, ValidationError, pokemon_page):
    class PokemonPage(BaseModel):
        model_config = ConfigDict(extra="forbid")
        results: list[Pokemon]

    try:
        parsed_page = PokemonPage.model_validate(pokemon_page)
    except ValidationError as e:
        print(e)
    return (parsed_page,)


@app.cell
def _(parsed_page):
    parsed_page
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Pokemon details

    Let's take another look at the Pokemon details. We'll collect the details from the first Pokemon in our list. The cell below shows a preview of all available columns, you can click any nested column to inspect the nested fields.
    """)
    return


@app.cell(hide_code=True)
def _(Pokemon, first_pokemon_parsed, requests):
    def get_pokemon_detail(pokemon: Pokemon) -> dict:
        # We can now access the pokemon attributes as Python objects
        response = requests.get(str(pokemon.url))
        return response.json()

    raw_detail = get_pokemon_detail(first_pokemon_parsed)
    return (raw_detail,)


@app.cell(hide_code=True)
def _(pl, raw_detail):
    pl.DataFrame([raw_detail])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 3: Modeling nested details

    We do not need to model every field from the API. Decide what fields are important for your graph and create an overview of what fields to keep. Pydantic skips extra API fields by default and does not store these in our model. This also prevents us from accidentally storing sensitive fields that may be present in the API response. Try completing the model below to include all fields that you want to keep/validate.
    """)
    return


@app.cell
def _(AnyHttpUrl, BaseModel, raw_detail):
    class PokemonType(BaseModel):
        name: str
        url: AnyHttpUrl

    class PokemonTypeSlot(BaseModel):
        slot: int
        type: PokemonType

    class PokemonDetail(BaseModel):
        id: int
        name: str
        height: int
        weight: int
        base_experience: int | None = None
        types: list[PokemonTypeSlot]
        # abilities: ...

    parsed_detail = PokemonDetail.model_validate(raw_detail)
    return PokemonDetail, parsed_detail


@app.cell
def _(parsed_detail):
    parsed_detail
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Simplifying for graph/properties use

    Pydantic models can preserve the nested API shape, but collector code often needs simpler derived values for the node/edge properties.

    The helper below converts a validated `PokemonDetail` into a compact dictionary that will be easier to use in later sections.
    """)
    return


@app.cell
def _(PokemonDetail, parsed_detail):
    def simplify_pokemon(detail: PokemonDetail) -> dict:
        return {
            "id": detail.id,
            "name": detail.name,
            "height": detail.height,
            "weight": detail.weight,
            "base_experience": detail.base_experience,
            "types": [item.type.name for item in detail.types],
            # "abilities": [item.ability.name for item in detail.abilities],
        }

    simplified_pokemon = simplify_pokemon(parsed_detail)
    return (simplified_pokemon,)


@app.cell
def _(simplified_pokemon):
    simplified_pokemon
    return


@app.cell(hide_code=True)
def _(pl, simplified_pokemons):
    pl.DataFrame(simplified_pokemons)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 4: Derived properties

    Add a derived property to `PokemonDetail` that returns only type names.

    Example:

    ```python
    @property
    def type_names(self) -> list[str]:
        return [item.type.name for item in self.types]
    ```

    Then update `simplify_pokemon` to use `detail.type_names`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Wrapping Up

    In this section, we used Pydantic to turn raw API dictionaries into typed resource models. Next, we will use DLT to replace our manual collection code while at the same time performing automated Pydantic validation.
    """)
    return


if __name__ == "__main__":
    app.run()
