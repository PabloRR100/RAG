from pydantic import BaseModel, ConfigDict

from rag_aas.schemas.ids import CollectionID


class CollectionMetadata(BaseModel):
    model_config = ConfigDict(extra="allow")


class CollectionCreate(BaseModel):
    name: str


class Collection(CollectionCreate):
    id: CollectionID
    metadata: CollectionMetadata

    

