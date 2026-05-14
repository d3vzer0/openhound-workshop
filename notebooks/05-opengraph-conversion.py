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
    # "polars>=1.40.1"
# ]
# ///

import marimo

__generated_with = "0.23.6"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    from dataclasses import dataclass, field
    from functools import lru_cache
    from pathlib import Path

    import dlt
    import duckdb
    import marimo as mo
    from dlt.extract.source import DltSource
    from dlt.sources.helpers.rest_client import RESTClient
    from dlt.sources.helpers.rest_client.paginators import JSONLinkPaginator
    from openhound.core.asset import BaseAsset, EdgeDef, NodeDef
    from openhound.core.collect import CollectContext
    from openhound.core.convert import ConvertContext
    from openhound.core.lookup import LookupManager
    from openhound.core.models.entries import Edge, EdgePath
    from openhound.core.models.entries_dataclass import (
        EdgeProperties,
        Node,
        NodeProperties,
    )
    from openhound.core.preproc import PreProcContext
    from openhound.core.progress import Progress
    from pydantic import AnyHttpUrl, BaseModel, field_serializer

    return (
        AnyHttpUrl,
        BaseAsset,
        BaseModel,
        CollectContext,
        ConvertContext,
        DltSource,
        EdgeDef,
        JSONLinkPaginator,
        LookupManager,
        Node,
        NodeDef,
        NodeProperties,
        Path,
        PreProcContext,
        Progress,
        RESTClient,
        dataclass,
        dlt,
        duckdb,
        field,
        field_serializer,
        lru_cache,
        mo,
    )


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Section 05: OpenGraph conversion

    In the previous section, we mapped the Pokemon collector onto the OpenHound `collect` and `preproc` phases:

    - `collect` writes raw API data to JSONL files.
    - `preproc` loads selected raw tables into DuckDB and prepares lookup data.
    - `convert` reads the raw data again and emits OpenGraph nodes and edges.

    This section focuses on the `convert` phase: turning validated Pydantic records into OpenGraph output.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Learning goals

    By the end of this section, you should be able to:

    - Explain how OpenHound converts DLT resources into OpenGraph output
    - Convert the Pydantic models into OpenHound assets
    - Add required node properties for all collected resources
    - Define stable OpenGraph node IDs
    - Use `self._lookup` during conversion
    - Emit edges from an asset model
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Conversion in the OpenHound workflow

    OpenHound conversion uses the same DLT source definition as collection, but with a different purpose. During `collect` the source tells DLT how to fetch raw records. During `convert`, the source tells OpenHound which collected tables should be parsed as OpenHound assets.

    An OpenHound asset is a Pydantic model with graph behavior:

    - Raw fields validate collected JSONL records
    - `as_node` returns the OpenGraph node for the record
    - `edges` returns relationships from that record to other nodes
    - `@app.asset(...)` documents which nodes and edges the asset emits
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.mermaid("""
    flowchart LR
        Raw[(pokemon_details JSONL)]:::storage
        Lookup[(lookup.duckdb)]:::optional
        Asset[Pokemon asset]:::step
        Node[OpenGraph node]:::output
        Edge[OpenGraph edges]:::output

        Raw --> Asset
        Lookup -.-> Asset
        Asset --> Node
        Asset --> Edge
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## The OpenHound app

    As before, each collector has exactly one `OpenHound` app instance. This is the object that owns the `collect`, `preproc`, and `convert` phase registrations, as well as the OpenGraph asset definitions. We already included the previous collection/preprocessing logic as part of the notebook that you can extend upon. Don't cheat and use this notebook while you're still finishing section 04-openhound!
    """)
    return


@app.cell(hide_code=True)
def _(
    AnyHttpUrl,
    BaseModel,
    DuckDBPyConnection,
    LookupManager,
    field_serializer,
    lru_cache,
    name,
):
    class Pokemon(BaseModel):
        name: str
        url: AnyHttpUrl

        @field_serializer("url")
        def serialize_url(self, url: AnyHttpUrl) -> str:
            return str(url)

    class PokemonType(BaseModel):
        name: str
        url: AnyHttpUrl

        @field_serializer("url")
        def serialize_url(self, url: AnyHttpUrl) -> str:
            return str(url)

    class PokemonTypeSlot(BaseModel):
        slot: int
        type: PokemonType


    class PokemonLookup(LookupManager):
        def __init__(self, client: DuckDBPyConnection, schema: str = "pokemon"):
            super().__init__(client, schema)
            self.schema = schema
            self.client = client

        @lru_cache
        def find_pokemon(self, poke_name: str) -> bool:
            result = self._find_single_object(
                f"SELECT * FROM {self.schema}.pokemon WHERE name = ?",
                [name],
            )
            return result

        @lru_cache
        def pokemon_types(self, pokemon_type: str) -> bool:
            result = self._find_all_objects(
                f"""
                SELECT
                    pokemon_name
                FROM 
                    {self.schema}.pokemon_types
                WHERE 
                    pokemon_type = ?
                """,
                [pokemon_type],
            )
            return result


    return PokemonLookup, PokemonTypeSlot


@app.cell(hide_code=True)
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

    return poke_transforms, pokemon_types


@app.cell(hide_code=True)
def _():
    from openhound.core.app import OpenHound

    POKEMON_API_BASE_URL = "https://pokeapi.co/api/v2/"

    app = OpenHound("pokemon", source_kind="Pokemon", help="OpenGraph collector for PokeAPI")
    return POKEMON_API_BASE_URL, app


@app.cell(hide_code=True)
def _():
    # app.collector(
    #     output_path=Path("/tmp/openhound"),
    #     resources=[], 
    #     progress=Progress.log,  
    # )
    return


@app.cell(hide_code=True)
def _():
    # app.preprocessor(
    #     input_path=Path("/tmp/openhound") / app.name,
    #     output_file=Path("lookup.duckdb"),
    #     progress=Progress.log,
    # )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Node and edge kinds
    Lets start by defining our node and edge kinds.
    A real collector usually stores kinds as constants in `kinds/nodes.py` and `kinds/edges.py`. For this workshop, we keep the constants as part of the Marimo notebook.

    `POKEMON` is the node kind emitted by our `Pokemon` asset. `SHARES_TYPE_WITH` is an example edge that connects one Pokemon to another Pokemon with a matching type resolved via the lookup database. To avoid conflicts, we suggest to prepend your node/edge values with a clear indicator of its origin. In this case, we add the `Poke_` prefix to both nodes/edges.
    """)
    return


@app.cell
def _():
    POKEMON = "Poke_Pokemon"
    SHARES_TYPE_WITH = "Poke_SharesTypeWith"
    return (POKEMON,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Graph base classes

    ### Required properties
    OpenHound uses dataclasses to define OpenGraph nodes, edges, and properties. The base `NodeProperties` class already requires every node to contain a `name`, `displayname`, and `environmentid` property.

    We add extension-specific properties in subclasses. In the case of the Pokemon dataset, let's define the `pokeapi_id` property to be required for all Pokemon-related assets.
    """)
    return


@app.cell
def _(NodeProperties, dataclass):
    @dataclass
    class PokeNodeProperties(NodeProperties):
        """Required properties for all PokeAPI nodes

        Attributes:
            pokeapi_id: The original row ID from the PokeAPI response.
        """
        pokeapi_id: int

    return (PokeNodeProperties,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Make sure to choose properties that:

    - Are present on **all** nodes from the service
    - Provide useful context for identification and filtering

    And make sure *not* to choose properties that:

    - Are specific only to a few nodes. Create a new dataclass that inherits `PokeNodeProperties` and extends it with asset-specific attributes
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### ID generation

    Each node is uniquely identified by an ID. You'll have to define how to generate a unique, reproducable ID. You can use OpenHound to generate a GUID based on a combination of node properties or re-use the ID from the source (if present).

    **Important**: avoid using raw integer IDs, these may not be consistent throughout the platform, can be based on incremented database IDs and/or may collide with nodes from other collectors.
    """)
    return


@app.cell
def _(Node, PokeNodeProperties, dataclass, field):
    @dataclass
    class PokeNode(Node):
        properties: PokeNodeProperties
        kinds: list[str]
        id: str = field(init=False)

        @staticmethod
        def guid(pokeapi_id: str) -> str:
                return Node.guid(pokeapi_id, "pokeapi")

        def __post_init__(self):
            self.id = self.guid(str(self.properties.pokeapi_id))

    return (PokeNode,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 1: Fixing the Node ID
    We didn't follow our own advise and used the PokeAPI ID to generate ID's for our nodes. These IDs are incremented integers and will cause conflicts. Fix the `PokeNode` class by generating a consistent, unique ID for each of our PokeAPI nodes.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## From Pydantic model to OpenGraph asset

    The original `PokemonDetail` model validates the raw `pokemon_details` records collected from PokeAPI. OpenHound requires a few additions to convert this data into nodes/edges:

    - It inherits `BaseAsset` instead of `BaseModel`
    - It is decorated with `@app.asset(...)` describing what node and edges are generated by this asset. Think about it this way: what OpenGraph assets can I generate based on a single row from the `pokemon_details` table?
    - It implements `as_node`
    - It implements `edges`


    An asset is not required to generate a node or edge, but the methods are expected to be implemented. Simply return `None` for `as_node` if no node is generated and return `[]` if no edges are generated.


    The raw fields should still match the collected JSONL schema.
    """)
    return


@app.cell
def _(
    BaseAsset,
    EdgeDef,
    NodeDef,
    POKEMON,
    PokeNode,
    PokeNodeProperties,
    PokemonTypeSlot,
    app,
    dataclass,
):
    @dataclass
    class PokemonProperties(PokeNodeProperties):
        """Required properties for all Pokemon nodes

        Attributes:
            height: The height of a Pokemon.
        """
        height: int


    @app.asset(
        node=NodeDef(
            kind=POKEMON,
            description="Pokemon collected from PokeAPI",
            icon="cog",
            properties=PokemonProperties,
        ),
        edges=[
            EdgeDef(
                start=POKEMON,
                end=POKEMON,
                kind="TODO",
                description="Pokemon shares at least one type with another Pokemon",
                traversable=False,
            )
        ],
    )
    class PokemonDetail(BaseAsset):
        id: int
        name: str
        height: int
        weight: int
        base_experience: int | None = None
        types: list[PokemonTypeSlot]

        @property
        def type_names(self) -> list[str]:
            return [item.type.name for item in self.types]

        @property
        def as_node(self) -> PokeNode:
            properties = PokemonProperties(
                name=self.name,
                displayname=self.name,
                height=self.height,
            )
            return PokeNode(properties=properties, kinds=[POKEMON])

        @property
        def edges(self):
            return []

    return (PokemonDetail,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 2: Completing the Pokemon Asset
    The Pokemon asset is still missing a lot of details. We defined PokemonProperties, but what other Pokemon attributes do we want to store as part of the node's properties? And we probably forgot to include a required field somewhere...

    Tip: OpenHound calls `as_node` during conversion, but we can inspect it directly in the notebook. The sample below uses a small PokeAPI-shaped record and validates it with the same `PokemonDetail` asset used by conversion. You can use the cell below to test if your changes to the `PokemonDetail` succesfully parses as a node.
    """)
    return


@app.cell
def _(PokemonDetail):
    sample_pokemon_detail = {
        "id": 1,
        "name": "bulbasaur",
        "height": 7,
        "weight": 69,
        "base_experience": 64,
        "types": [
            {
                "slot": 1,
                "type": {
                    "name": "grass",
                    "url": "https://pokeapi.co/api/v2/type/12/",
                },
            },
            {
                "slot": 2,
                "type": {
                    "name": "poison",
                    "url": "https://pokeapi.co/api/v2/type/4/",
                },
            },
        ],
    }

    sample_pokemon_asset = PokemonDetail.model_validate(sample_pokemon_detail)
    sample_pokemon_asset.as_node
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Lookup during conversion

    In section 04 we created a `pokemon_types` DuckDB table during the `preprocessing` phase. Additionally, we implemented a `PokemonLookup` class with the `pokemon_types` method to find all pokemons belonging to a specific type. We can call this lookup method during conversion using the `self._lookup.pokemon_types`.

    The lookup below finds all other Pokemon with the same type. This is a relatively small example, lookups are often used to resolve group membership, ownership or other relationships that require more complex conditions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Previewing lookup data

    The real conversion phase injects `PokemonLookup` into each asset as `self._lookup`. To preview what data is returned by our `pokemon_types(pokemon_type: str)` lookup method, lets take a look at the cell below. And while we're add it, lets try using some of the built-in Marimo features for interactivity. See what happens when you change the `pokemon_type` drop-down selection.
    """)
    return


@app.cell(hide_code=True)
def _(duckdb):
    duckdb_client = duckdb.connect("lookup.duckdb")
    return (duckdb_client,)


@app.cell(hide_code=True)
def _(duckdb_client, mo, pokemon_types):
    unique_pokemon_types = mo.sql(
        f"""
        select distinct(pokemon_type) from pokemon_types
        """,
        engine=duckdb_client
    )
    return (unique_pokemon_types,)


@app.cell(hide_code=True)
def _(mo, unique_pokemon_types):
    select_type = mo.ui.dropdown.from_series(unique_pokemon_types["pokemon_type"])
    select_type
    return (select_type,)


@app.cell
def _(PokemonLookup, duckdb_client, select_type):
    pokemon_lookup = PokemonLookup(duckdb_client)
    [name for (name,) in pokemon_lookup.pokemon_types(select_type.selected_key)]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Exercise 3: Adding  edges

    Modify `PokemonDetail.edges` so it creates edges with other Pokemons sharing the same type. Here is an example from another collector to get you started:

    ```python
    @property
    def _groups_memberships(self):
        for (group_id,) in self._lookup.groups(self.hostname):
            start = EdgePath(value=self.as_node.id, match_by="id")
            end = EdgePath(value=group.id, match_by="id")
            yield Edge(kind=ek.MemberOf, start=start, end=end)

    @property
    def edges(self):
        yield from self._groups_membership

    ```
    Some things to think about:
    - Should you generate multiple edges to the same Pokemon if they share multiple types?
    - What edge properties are useful to add?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Source definition for conversion

    OpenHound conversion matches assets to source resources by looking at the Pydantic model configured on the resource or transformer.

    That means `pokemon_details` must use `columns=PokemonDetail`. During collection, DLT uses this model for validation. During conversion, OpenHound uses it to know that records from the `pokemon_details` table should be converted with the `PokemonDetail` asset.

    First lets re-define our Pokemon (details) collector below.
    """)
    return


@app.cell
def _(
    CollectContext,
    DltSource,
    JSONLinkPaginator,
    POKEMON_API_BASE_URL,
    PokemonDetail,
    PreProcContext,
    RESTClient,
    app,
    dlt,
    poke_transforms,
):
    pokemon_client = RESTClient(
        base_url=POKEMON_API_BASE_URL,
        paginator=JSONLinkPaginator(next_url_path="next"),
    )

    @app.resource(table_name="pokemon")
    def pokemon():
        for page in pokemon_client.paginate("pokemon", data_selector="results"):
            yield page


    @app.transformer(
        table_name="pokemon_details",
        parallelized=True,
        columns=PokemonDetail

    )
    def pokemon_details(pokemons: list):
        @dlt.defer
        def _get_pokemon_details(_pokemon):
            return pokemon_client.get(_pokemon["url"]).json()

        for _pokemon in pokemons:
            yield _get_pokemon_details(_pokemon)


    @app.source(name="poke_api", max_table_nesting=0)
    def source():
        return pokemon | pokemon_details


    @app.collect()
    def collect(ctx: CollectContext) -> DltSource:
        return source()

    @app.preproc(transformer=poke_transforms)
    def preproc(ctx: PreProcContext) -> dict[str, str]:
        return {
            "pokemon_details": "pokemon_details",
        }


    return (source,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Convert phase registration

    The `@app.convert` decorator registers the conversion phase. Any additional lookup classess are added via the decorator's `lookup=` parameter.

    The convert function should return two values:

    - The original DLT source which collected tables should be converted
    - An extras dictionary made available to every asset via `self._extras`
    """)
    return


@app.cell
def _(ConvertContext, DltSource, app, source):
    @app.convert()
    def convert(ctx: ConvertContext) -> DltSource:
        return source(), {}

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Exercise 4: Converting to OpenGraph
    Take a look at the convert function above. Are we missing anything? After adding your changes, the extension should now be listed as a converter when running:

    `openhound convert --help`

    To convert collected Pokemon data from `/tmp/openhound/pokemon` and write OpenGraph output to `/tmp/openhound/opengraph`:

    `openhound convert pokemon /tmp/openhound/pokemon /tmp/openhound/opengraph`

    Since we're running inside a Marimo notebook, we'll call the registered converter directly. This expects the collection and preprocessing phases from section 04 to have completed successfully.

    **Note:** If you don't have access to the collected resources/lookup anymore, disable the cell below and re-run collection/processing.
    """)
    return


@app.cell(disabled=True, hide_code=True)
def _(Path, Progress, app):
    app.collector(
        output_path=Path("/tmp/openhound"),
        resources=[], 
        progress=Progress.log,  
    )

    app.preprocessor(
        input_path=Path("/tmp/openhound") / app.name,
        output_file=Path("lookup.duckdb"),
        progress=Progress.log,
    )
    return


@app.cell
def _(Path, Progress, app):
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
    ## Exercise 5: Inspect the OpenGraph output

    After conversion finishes succesfully, inspect the generated OpenGraph files inside the `./opengraph` directory. You can use the built-in Marimo file browser.

    Things to check:

    - Pokemon nodes include the graph properties you want
    - `SharesTypeWith` edges point from one Pokemon node ID to another Pokemon node ID
    - Re-running conversion produces the same node IDs

    When you're happy with the output, try uploading the output to BloodHound!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ## Wrapping up

    You have now implemented the full OpenHound workflow:

    - `collect`: API data to raw JSONL
    - `preproc`: raw JSONL to DuckDB lookup data
    - `convert`: raw JSONL plus lookup data to OpenGraph nodes and edges

    Now lets continue to the next section where we instruct a coding agent to extend the graph with more nodes and edges.
    """)
    return


if __name__ == "__main__":
    app.run()
