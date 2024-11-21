from typing import Any, TypeAlias, Optional
from langchain_core.documents import Document as LangchainDocument
# from langchain_core.embeddings import Embeddings as LangchainEmbeddings
from pydantic import BaseModel

from rag_aas.schemas.ids import CollectionID, DocumentID


Content: TypeAlias = str
Embedding: TypeAlias = list[float]
DocumentMetadata: TypeAlias = dict[str, Any]
    

class DocumentCreate(BaseModel):
    content: Content
    collection_id: CollectionID
    metadata: Optional[DocumentMetadata] = None


class DocumentAdd(DocumentCreate):
    embedding: Embedding


class Document(DocumentCreate, DocumentAdd):
    id: DocumentID

    @classmethod
    def from_langchain(cls, document: LangchainDocument) -> "Document":
        return cls(
            id=document.id,
            content=document.content,
            collection_id=document.collection_id,
            metadata=document.metadata,
            embedding=document.embedding
        )
