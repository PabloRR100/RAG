from pydantic import BaseModel


class SearchQuery(BaseModel):
    query: str
    collection_id: int
    limit: int = 10
    offset: int = 0

