from typing import Any, TypeAlias, Optional
from pydantic import BaseModel


DocumentMetadata: TypeAlias = dict[str, Any]
    

class DocumentCreate(BaseModel):
    content: str
    collection_id: int
    metadata: Optional[DocumentMetadata] = None


class Document(DocumentCreate):
    id: int

