import dlt
from dlt.sources.helpers.rest_client.client import RESTClient
from dlt.sources.helpers.rest_client.paginators import JSONLinkPaginator

from openhound_pokemon.main import app
from openhound_pokemon.models import PokeAPIEnvironment, Pokemon, PokemonDetail


POKEMON_API_BASE_URL = "https://pokeapi.co/api/v2/"


@app.resource(table_name="environment", columns=PokeAPIEnvironment)
def environment():
    yield {"name": "pokeapi"}


@app.resource(table_name="pokemon", columns=Pokemon)
def pokemon(client: RESTClient):
    for page in client.paginate("pokemon", data_selector="results"):
        yield page


@app.transformer(
    table_name="pokemon_details",
    parallelized=True,
    columns=PokemonDetail,
    max_table_nesting=0,
)
def pokemon_details(pokemons: list, client: RESTClient):
    @dlt.defer
    def get_pokemon_details(pokemon_record):
        return client.get(pokemon_record["url"]).json()

    for pokemon_record in pokemons:
        yield get_pokemon_details(pokemon_record)


@app.source(name="poke_api", max_table_nesting=0)
def source():
    client = RESTClient(
        base_url=POKEMON_API_BASE_URL,
        paginator=JSONLinkPaginator(next_url_path="next"),
    )
    pokemon_resource = pokemon(client)
    return (
        environment,
        pokemon_resource | pokemon_details(client),
    )
