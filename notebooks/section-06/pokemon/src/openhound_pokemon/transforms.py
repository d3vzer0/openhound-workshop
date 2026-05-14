import duckdb


def pokemon_types(con: duckdb.DuckDBPyConnection, schema: str = "pokemon") -> None:
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


def transforms(con: duckdb.DuckDBPyConnection, schema: str = "pokemon") -> None:
    pokemon_types(con, schema)
