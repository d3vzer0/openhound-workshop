from functools import lru_cache

import duckdb
from openhound.core.lookup import LookupManager


class PokemonLookup(LookupManager):
    def __init__(self, client: duckdb.DuckDBPyConnection, schema: str = "pokemon"):
        super().__init__(client, schema)
        self.schema = schema
        self.client = client

    @lru_cache
    def pokemon_with_type(self, pokemon_type: str) -> list:
        return self._find_all_objects(
            f"""
            SELECT pokemon_id
            FROM {self.schema}.pokemon_types
            WHERE pokemon_type = ?
            ORDER BY pokemon_id
            """,
            [pokemon_type],
        )
