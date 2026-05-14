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
app = marimo.App(
    width="medium",
    layout_file="layouts/04-openhound.slides.json",
)


@app.cell
def _():
    import marimo as mo
    from pathlib import Path
    import dlt
    import polars as pl

    from openhound.core.progress import Progress
    from dlt.extract.source import DltSource
    from dlt.sources.helpers.rest_client import RESTClient
    from dlt.sources.helpers.rest_client.paginators import JSONLinkPaginator
    from openhound.core.collect import CollectContext
    from openhound.core.preproc import PreProcContext
    from openhound.core.convert import ConvertContext

    return (
        CollectContext,
        DltSource,
        JSONLinkPaginator,
        Path,
        PreProcContext,
        Progress,
        RESTClient,
        mo,
        pl,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Section 04: OpenHound specifics

    In the previous sections we built the collector pieces one by one:

    - We collected Pokemon data manually with `requests`
    - We used Pydantic to validate API responses
    - We used DLT resources, transformers, sources, and pipelines

    OpenHound is the layer that turns those pieces into a repeatable collector workflow for OpenGraph. This section focuses on OpenHound-specific structure and behavior. The next section will focus on actual graph modeling.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Learning goals

    By the end of this section, you should be able to:

    - Implement the OpenHound `collect -> preproc -> convert` workflow
    - Explain why logging and exceptions become easier
    - Explain when preprocessing and lookups are useful
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## What OpenHound adds

    OpenHound standardizes how DLT resources, transformers and sources are used for graph collection and conversion. Here are some of the differences:

    - Pipeline sources, destinations and configurations are standardized
    - Logging and resource collection failures are handled by OpenHound
    - Pydantic models are included to automatically validate OpenGraph output
    - OpenHound is able to generate (zensical) documentation for your extension, including graph examples, in/outgoing edges, node icons etc.
    - Every collector exposes multiple CLI commands and can be run seperately
    - OpenHound adds standardized lookup functionality using DuckDB

    OpenHound organizes DLT and Pydantic for OpenGraph collection and conversion OpenHound, it does not replace DLT or Pydantic.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Collect, preprocess and convert

    Every OpenHound collector follows the same high-level workflow.

    | Phase | Purpose | Pokemon example |
    |---|---|---|
    | `collect` | Collect upstream API data and write raw (compressed) JSONL | Run the DLT Pokemon source. |
    | `preproc` | Optionally load raw tables into DuckDB and build lookup data | Build a unique list of Pokemon types |
    | `convert` | Read collected data and emit OpenGraph nodes and edges | Emit Pokemon and PokemonType OpenGraph objects |

    Splitting the three phases is important. Some nodes/edges require the full dataset to be available and splitting the phases lets you debug collection issues separately from graph conversion issues.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.mermaid("""
    flowchart LR
        Collect([Collect]):::step
        Preprocess([Preprocess]):::step
        Convert([Convert]):::step

        Raw[(JSONL/Parquet)]:::storage
        DuckDB[(DuckDB)]:::optional

        OpenGraph[OpenGraph]:::output

        Collect --> Raw
        Raw --> Preprocess
        Preprocess -.-> DuckDB
        DuckDB -.-> Convert
        Preprocess --> Convert
        Convert --> OpenGraph
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Collector structure

    A typical OpenHound collector implements (at least) the following files:

    ```text
    src/openhound_pokemon/
      main.py
      source.py
      graph.py
      lookup.py (optional)
      transforms.py (optional)
      kinds/
        nodes.py
        edges.py
      models/
        pokemon.py
    extension.yaml
    ```

    You won't have to remember this for now, during this workshop we'll create an OpenHound collector as part of this notebook.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The OpenHound app

    Each collector implements exactly one `OpenHound` app instance, which is usually defined in the `main.py` file. This is what allows OpenHound to discover the collector and each of the phases.

    **Important**:
    - Keep exactly one app instance per collector
    - Define a `source_kind` for your collector. This will be used as a node kind for all the collected resources in BloodHound.
    """)
    return


@app.cell
def _():
    from openhound.core.app import OpenHound

    app = OpenHound("pokemon", source_kind="Pokemon", help="OpenGraph collector for PokeAPI")
    return (app,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Defining the source

    The DLT source still look similar to normal DLT code, with the exception that the `@dlt` decorators are replaced with `@app` decorators. This allows the OpenHound framework discover which source/resource/transformer belongs to what `OpenHound` app instance, while at the same time adding custom exception handling/logging during resource collection.
    """)
    return


@app.cell(hide_code=True)
def _(LoadInfo):
    def extracted_resources(load_info: LoadInfo) -> list[str]:
        all_resources = []
        for package in load_info.load_packages:
            for job in package.jobs["completed_jobs"]:
                table = job.job_file_info.table_name
                all_resources.append(table)

        return all_resources

    return (extracted_resources,)


@app.cell(hide_code=True)
def _(JSONLinkPaginator, RESTClient):
    POKEMON_API_BASE_URL = "https://pokeapi.co/api/v2/"
    pokemon_client = RESTClient(
        base_url=POKEMON_API_BASE_URL,
        paginator=JSONLinkPaginator(next_url_path="next"),
    )
    return (pokemon_client,)


@app.cell
def _(app, pokemon_client):
    @app.resource(table_name="pokemon")
    def pokemon():
        for page in pokemon_client.paginate("pokemon", data_selector="results"):
            yield page

    return (pokemon,)


@app.cell
def _(app, pokemon):
    @app.source(name="poke_api", max_table_nesting=0)
    def source():
        return pokemon


    return (source,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Collect phase

    The collect phase returns the DLT source from `source.py`.

    How this is different compared to plain DLT:
    - You do not manually configure the pipeline in every script. The pipeline is consistent for all collectors
    - The raw collection output goes where the next OpenHound phase expects it
    """)
    return


@app.cell
def _(CollectContext, DltSource, app, source):
    @app.collect()
    def collect(ctx: CollectContext) -> DltSource:
        return source()


    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Thats everything needed to start running the OpenHound collection phase. When using the OpenHound CLI, your extension should now be listed as a collector when running:

    `openhound collect --help`

    And to start collecting Pokemon data to the /tmp/openhound directory:

    `openhound collect pokemon /tmp/openhound`

    Since we're running inside of a Marimo notebook, we'll have to run the collection phase manually. The cell below mimicks the behaviour of running the `openhound collect pokemon /tmp/openhound` command
    """)
    return


@app.cell
def _(Path, Progress, app, extracted_resources):
    load_info = app.collector(
        output_path=Path("/tmp/openhound"),
        resources=[], 
        progress=Progress.log,  
    )
    extracted_resources(load_info)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 1: Update the resources/transformers
    The `poke_api` source is still lacks the Pokemon details transformer. Update the OpenHound resource collectors to match the implementation from the previous section of the workshop (03-dlt.py)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Preproc phase

    The `preproc` phase is optional. Use it when conversion needs data that is easier to query from DuckDB than keeping everything in memory for the full duration of the pipeline.

    Common reasons to use `preproc`:

    - Join data from multiple collected tables
    - Create derived lookup tables
    - Resolve relationships during conversion

    Pokemon example:
    - Raw `pokemon_details` records contain nested `types`.
    - The graph should contain one `PokemonType` node per unique type.
    - A preprocessing step can create a `pokemon_types` table with unique type names.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Preproc registration

    The preproc function maps DuckDB table names to collected JSONL table names. The example below loads the pokemon_details files into the DuckDB `pokemon_details` table. This data can later be used during the convert phase. The `@app.preproc` decorator also accepts the optional `transformer` parameter. The value should be a reference to a Python function which executes DuckDB SQL queries. More about this later.

    Important nuances:
    - Only tables listed here are loaded into the preprocessing DuckDB database
    - Use `transformer=....` only when you want to apply additional SQL-based transformations.
    """)
    return


@app.cell
def _(PreProcContext, app):
    @app.preproc()
    def preproc(ctx: PreProcContext) -> dict[str, str]:
        return {
            "pokemon_details": "pokemon_details",
        }


    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The extension should now be listed as a preprocessor when running:

    `openhound preprocess --help`

    To start preprocessing Pokemon data from the /tmp/openhound/poke_api directory (poke_api is appended to the output path by the collect phase):

    `openhound preprocess pokemon /tmp/openhound/poke_api`

    If no output path is specified, a `lookup.duckdb` file will be created in the current working directory. Since we're running inside of a Marimo notebook, we'll have to run the preprocessing phase manually. The cell below mimicks the behaviour of running the openhound preprocess pokemon /tmp/openhound/pokemon command
    """)
    return


@app.cell
def _(Path, Progress, app):
    preproc_load_info = app.preprocessor(
        input_path=Path("/tmp/openhound") / app.name,
        output_file=Path("lookup.duckdb"),
        progress=Progress.log,
    )
    preproc_load_info
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 2: Looking up the lookup
    Marimo allows you to explore data from most common databases. This obiously also includes local DuckDB files. Try connecting to `lookup.duckdb` and see what changes in Marimo (hint: check Marimo variables and datasources)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Transforms

    Optionally, a `transforms.py` contains DuckDB SQL that creates derived and optimized tables that may be useful for lookups during the convert phase.

    A Pokemon type transform could look like the cell below, where we create a pokemon_types table with the unnested Pokemon types. Keep transforms small and focused. Transforms should prepare or improve lookup data.
    """)
    return


@app.cell
def _(duckdb):
    def pokemon_types(con: duckdb.DuckDBPyConnection, schema: str):
        con.execute(f"""
        CREATE OR REPLACE TABLE {schema}.pokemon_types AS
        SELECT
            p.id AS pokemon_id,
            p.name AS pokemon_name,
            CAST(type_json.value->>'slot' AS INTEGER) AS type_slot,
            type_json.value->'type'->>'name' AS pokemon_type
        FROM {schema}.pokemon_details AS p,
            json_each(p.types) AS type_json
        """)

    def poke_transforms(con: duckdb.DuckDBPyConnection, schema: str = "pokemon") -> None:
        pokemon_types(con, schema)
    

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 3: Adding transforms
    Modify the `preproc` phase by adding the `poke_transforms` function as an additional transformer. Now use Marimo to inspect the changes applied to our `lookup.duckdb` database. Can you run a query to find Pokemons with more than 1 type?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## LookupManager

    Now that we've implemented the preprocessing phase we need to define a dedicated lookup class that inherits `LookupManager`. All methods implemented by the custom lookup can later be used when we convert our raw resources to OpenGraph nodes and edges.

    Note: The `schema` should match with our collector name
    """)
    return


@app.cell
def _(DuckDBPyConnection, name):
    from functools import lru_cache

    from openhound.core.lookup import LookupManager


    class PokemonLookup(LookupManager):
        def __init__(self, client: DuckDBPyConnection, schema: str = "pokemon"):
            super().__init__(client, schema)
            self.schema = schema
            self.client = client

        @lru_cache
        def find_pokemon(self, poke_name: str) -> bool:
            result = self._find_single_object(
                f"select * from {self.schema}.pokemon where name = ?",
                [name],
            )
            return result

        @lru_cache
        def pokemon_types(self, var1: str, var2: str) -> bool:
            result = self._find_all_objects(
                f"... where var1 = ? AND var2 = ?",
                [var1, var2],
            )
            return result

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The inherited `LookupManager` exposes two methods:
    - `_find_single_object`: Returns a single row matching the query or None when no results are found
    - `_find_all_objects`: Returns all rows matching the query or an empty list when no results are found

    Why creating a dedicated LookupManager with pre-defined queries is important:
    - Models do not need to know DuckDB query details
    - Cross-table logic has one clear place
    - Cached methods avoid repeating the same query
    - Missing lookup results can be handled consistently by OpenHound
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 4: Finish the lookup
    The example `PokemonLookup` above is not finished yet. Modify the `pokemon_types` method to query all Pokemon matching a specific input type.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## OpenHound logging


    Some things you'll need to know when debugging your collector:

    - Logs are stored in JSONL format by default
    - Each collector gets its own log file stored as `ext_{name}.log`
    - The base OpenHound framework logs are stored as `openhound.log`
    - When a specic resource/transformer raises an error, OpenHound will log the exception message and not stop the full pipeline.

    We can use Marimo's dataframe render to preview our Pokemon pipeline. Take a look at the openhound and pokemon log preview below!
    """)
    return


@app.cell
def _(mo, pl):
    poke_log_path = "/home/marimo/.local/share/openhound/logs/ext_pokemon.log"
    log_preview_df = pl.scan_ndjson(poke_log_path).head(100).collect()
    mo.ui.dataframe(log_preview_df)
    return


@app.cell
def _(mo, pl):
    base_log_path = "/home/marimo/.local/share/openhound/logs/openhound.log"
    base_log_preview_df = pl.scan_ndjson(base_log_path).head(100).collect()
    mo.ui.dataframe(base_log_preview_df)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Wrapping Up

    In this section we mapped the DLT collector pattern into OpenHound's collector structure.

    Key takeaways:

    - OpenHound organizes collectors into `collect`, `preproc`, and `convert` phases
    - There is single OpenHound app and phase registration.
    - Preprocessing and lookups simplifies cross-table conversion logic

    Next, we will define Pokemon graph nodes, edge kinds, stable IDs, and conversion behavior.
    """)
    return


if __name__ == "__main__":
    app.run()
