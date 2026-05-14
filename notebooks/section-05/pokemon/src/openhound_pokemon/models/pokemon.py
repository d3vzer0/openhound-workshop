from dataclasses import dataclass

from openhound.core.asset import BaseAsset, EdgeDef, NodeDef
from openhound.core.models.entries import Edge, EdgePath

from openhound_pokemon.graph import (
    PokeNode,
    PokeNodeProperties,
    pokeapi_environment_id,
    pokemon_node_id,
)
from openhound_pokemon.kinds import edges as ek
from openhound_pokemon.kinds import nodes as nk
from openhound_pokemon.main import app
from openhound_pokemon.models.common import NamedAPIResource, PokemonTypeSlot


class Pokemon(NamedAPIResource):
    pass


@dataclass
class PokemonProperties(PokeNodeProperties):
    """Properties for Pokemon nodes.

    Attributes:
        node_id: Stable OpenGraph node ID derived from the PokeAPI Pokemon ID.
        pokeapi_id: The original row ID from the PokeAPI response.
        height: The height of a Pokemon.
        weight: The weight of a Pokemon.
        base_experience: The base experience gained for defeating this Pokemon.
    """

    height: int
    weight: int
    base_experience: int | None = None


@app.asset(
    node=NodeDef(
        kind=nk.POKEMON,
        description="Pokemon collected from PokeAPI",
        icon="cog",
        properties=PokemonProperties,
    ),
    edges=[
        EdgeDef(
            start=nk.POKEMON,
            end=nk.POKEMON,
            kind=ek.SHARES_TYPE_WITH,
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
            node_id=pokemon_node_id(self.id),
            name=self.name,
            displayname=self.name,
            environmentid=pokeapi_environment_id(),
            pokeapi_id=self.id,
            height=self.height,
            weight=self.weight,
            base_experience=self.base_experience,
        )
        return PokeNode(properties=properties, kinds=[nk.POKEMON])

    @property
    def edges(self):
        seen_targets: set[str] = set()
        for pokemon_type in self.type_names:
            for target_id, in self._lookup.pokemon_with_type(pokemon_type):
                if int(target_id) == self.id:
                    continue

                target_node_id = pokemon_node_id(target_id)
                if target_node_id in seen_targets:
                    continue

                seen_targets.add(target_node_id)
                yield Edge(
                    kind=ek.SHARES_TYPE_WITH,
                    start=EdgePath(value=self.as_node.id, match_by="id"),
                    end=EdgePath(value=target_node_id, match_by="id"),
                )
