# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "dlt==1.26.0",
#     "marimo>=0.23.6",
#     "openhound==0.1.4",
#     "pydantic==2.13.3",
#     "openhound-pokemon==0.1.0",
#     "duckdb==1.5.2",
#     "polars==1.40.1",
# ]
# [tool.uv.sources]
# openhound-pokemon = { path = "./section-06/pokemon", editable = true }
# ///

import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    from dataclasses import dataclass, field
    from pathlib import Path
    from openhound.core.lookup import LookupManager
    import polars as pl
    import dlt
    import marimo as mo
    from openhound_pokemon.main import app
    from dlt.extract.source import DltSource
    from dlt.sources.helpers.rest_client import RESTClient
    from dlt.sources.helpers.rest_client.paginators import JSONLinkPaginator
    from openhound.core.asset import BaseAsset, EdgeDef, NodeDef
    from openhound.core.collect import CollectContext
    from openhound.core.convert import ConvertContext
    from openhound.core.models.entries import Edge, EdgePath
    from openhound.core.models.entries_dataclass import Node, NodeProperties
    from openhound.core.preproc import PreProcContext
    from openhound.core.progress import Progress
    from pydantic import AnyHttpUrl, BaseModel, field_serializer
    from functools import lru_cache


    return Path, Progress, app, mo, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Section 06: Working with agents

    In the previous sections we built a small OpenHound collector. In this final section we'll use that collector as a starting point for agent-assisted development.

    The goal is to give an agent enough context to extend the collector and implement additional nodes and edges. If you cloned the original Github repository for this workshop, a set of Marimo and OpenHound agent skills are included to optimize the process.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Learning goals

    By the end of this section you should be able to:

    - Write a focused prompt for a coding agent
    - Point an agent at local API documentation
    - Ask for specific OpenHound collector changes
    - Review generated graph nodes, edges, and IDs
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Agent workflow

    Agents work best when you give them a narrow task and clear criteria.

    A useful workflow for this notebook:

    - Pick one graph question, such as "Which games does this Pokemon appear in?"
    - Find the relevant endpoint in `./section-06/pokeapi.md`
    - Ask the agent to add only the needed resource, model, node and edges
    - Ask the agent to avoid unrelated refactors
    - Ask the agent to validate the notebook before finishing
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## API documentation

    The PokeAPI endpoint documentation is available locally at `./section-06/pokeapi.md`

    Useful Pokemon-related endpoints include:

    - `Items`
    - `Games`
    - `Encunters`
    - `Locations`
    - `Evolution`

    The agent should read the relevant section from the markdown file before changing any code and refer to the openhound skill for any openhound-related changes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Sample prompt

    Use this as a starting point and adjust the goal for the resource you want to add:

    ```text
    You are working on a creating Pokemon graph database. The current Pokemon extension for OpenHound collects pokemon details from the PokeAPI service. OpenHound converts these raw resources into nodes and edges for BloodHound/OpenGraph.

    The current implementation only collects the basic details about a Pokemon. I want to extend the graph by collecting more relevant resources.

    Context:
    - The PokeAPI documentation can be found in `./notebooks/section-06/pokeapi.md`
    - The Pokemon OpenHound extension code is located at `./notebooks/section-06/pokemon/src`

    Goal:
    Add Pokemon Games collection and graph conversion.

    Requirements:
    - Read the `Games` section from `pokeapi.md` documentation.
    - Add a DLT/OpenHound transformer that collects each Game from the relevant API endpoint.
    - Add a Pydantic/OpenHound asset for the Pokemon game.
    - Emit a `Poke_Game` node with stable string IDs.
    - Investigate if an edge can be created from a Pokemon to the Game.
    - Add only the minimal transforms/lookups needed. Do not add a lookup if none are needed.
    - Do not refactor unrelated code.

    Validation:
    - Report what changed and any checks that could not be run. Describe how any edge/relationship are defined.
    ```
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Collect data

    Run the collection pipeline when anything changed to the resource collection components.

    The equivalent CLI commands are:

    ```bash
    openhound collect pokemon /tmp/openhound
    ```
    """)
    return


@app.cell
def _(Path, Progress, app):
    app.collector(
        output_path=Path("/tmp/openhound"),
        resources=[],
        progress=Progress.log,
    )
    return


@app.cell
def _(pl):
    poke_details_path = "/tmp/openhound/pokeapi/pokemon_details/"
    log_preview_df = pl.scan_ndjson(poke_details_path).head(100).collect()
    return (log_preview_df,)


@app.cell
def _(log_preview_df):
    log_preview_df
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Convert data

    Run the conversion pipeline when anything changed to the resource conversion components.

    The equivalent CLI commands are:

    ```bash
    openhound preprocess pokemon /tmp/openhound/pokemon
    openhound convert pokemon /tmp/openhound/pokemon ./opengraph
    ```
    """)
    return


@app.cell
def _(Path, Progress, app):
    app.preprocessor(
        input_path=Path("/tmp/openhound") / app.name,
        output_file=Path("lookup.duckdb"),
        progress=Progress.log,
    )

    app.converter(
        input_path=Path("/tmp/openhound") / app.name,
        output_path=Path("./opengraph"),
        lookup_file=Path("lookup.duckdb"),
        progress=Progress.log,
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Review checklist

    After the agent modifies this notebook, review the changes before accepting them:

    - Did it read `notebooks/section-06/pokeapi.md`?
    - Did it use the OpenHound skill?
    - Did it add only the requested resource(s)?
    - Do new `NodeDef(...)` and `EdgeDef(...)` declarations match the emitted graph output?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Congrats! Thats it for now.
    Here is a picture of Charmander, just for you.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image("https://upload.wikimedia.org/wikipedia/en/5/56/Charmander.png")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
