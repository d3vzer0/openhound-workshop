from dlt.extract.source import DltSource
from openhound.core.app import OpenHound
from openhound.core.collect import CollectContext
from openhound.core.convert import ConvertContext
from openhound.core.preproc import PreProcContext

from openhound_pokemon.lookup import PokemonLookup
from openhound_pokemon.transforms import transforms


app = OpenHound("pokemon", source_kind="Pokemon", help="OpenGraph collector for PokeAPI")


@app.collect()
def collect(ctx: CollectContext) -> DltSource:
    from openhound_pokemon.source import source as poke_source

    return poke_source()


@app.preproc(transformer=transforms)
def preproc(ctx: PreProcContext) -> dict[str, str]:
    return {
        "pokemon_details": "pokemon_details",
    }


@app.convert(lookup=PokemonLookup)
def convert(ctx: ConvertContext) -> tuple[DltSource, dict]:
    from openhound_pokemon.source import source as poke_source

    return poke_source(), {}


from openhound_pokemon import models as models  # noqa: E402,F401
