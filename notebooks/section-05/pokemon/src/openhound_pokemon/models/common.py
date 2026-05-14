from pydantic import AnyHttpUrl, BaseModel, field_serializer


class NamedAPIResource(BaseModel):
    name: str
    url: AnyHttpUrl

    @field_serializer("url")
    def serialize_url(self, url: AnyHttpUrl) -> str:
        return str(url)


class PokemonTypeSlot(BaseModel):
    slot: int
    type: NamedAPIResource
