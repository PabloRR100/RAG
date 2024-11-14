from pydantic import BaseModel


class CollectionCreate(BaseModel):
    name: str


class Collection(CollectionCreate):
    id: int

