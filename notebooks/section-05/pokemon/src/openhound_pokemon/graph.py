from dataclasses import dataclass, field

from openhound.core.models.entries_dataclass import Node, NodeProperties


@dataclass
class PokeNodeProperties(NodeProperties):
    """Required properties for all PokeAPI nodes.

    Attributes:
        node_id: Stable OpenGraph node ID derived from PokeAPI values.
        pokeapi_id: The original row ID from the PokeAPI response, if available.
    """

    node_id: str
    pokeapi_id: int | None = field(default=None, kw_only=True)


@dataclass
class PokeNode(Node):
    properties: PokeNodeProperties
    kinds: list[str]
    id: str = field(init=False)

    def __post_init__(self):
        self.id = self.properties.node_id


def pokeapi_environment_id() -> str:
    return PokeNode.guid("pokeapi", "environment", "pokeapi")


def pokemon_node_id(pokeapi_id: int | str) -> str:
    return PokeNode.guid("pokeapi", "pokemon", str(pokeapi_id))
