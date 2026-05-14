from dataclasses import dataclass

from openhound.core.asset import BaseAsset, NodeDef

from openhound_pokemon.graph import PokeNode, PokeNodeProperties, pokeapi_environment_id
from openhound_pokemon.kinds import nodes as nk
from openhound_pokemon.main import app


@dataclass
class PokeAPIEnvironmentProperties(PokeNodeProperties):
    """Properties for the PokeAPI environment node.

    Attributes:
        node_id: Stable OpenGraph node ID for the PokeAPI environment.
        pokeapi_id: The original row ID from the PokeAPI response, if available.
    """


@app.asset(
    node=NodeDef(
        kind=nk.POKEAPI,
        description="PokeAPI environment",
        icon="database",
        properties=PokeAPIEnvironmentProperties,
    )
)
class PokeAPIEnvironment(BaseAsset):
    name: str = "pokeapi"

    @property
    def as_node(self) -> PokeNode:
        properties = PokeAPIEnvironmentProperties(
            node_id=pokeapi_environment_id(),
            name=self.name,
            displayname="PokeAPI",
            environmentid=pokeapi_environment_id(),
        )
        return PokeNode(properties=properties, kinds=[nk.POKEAPI])

    @property
    def edges(self):
        return []
