from abc import ABC, abstractmethod

from pydantic import BaseModel, Field, model_validator

from schemas.collection import Collection, CollectionCreate
from schemas.config import LOG, VectorStoreSettings
from schemas.document import Document, DocumentCreate


class Manager(ABC, BaseModel):
    """
    Abstract class for managing entities in the database
    """
    type: str = Field(discriminator=True)
    config: VectorStoreSettings 

    @model_validator(mode="before")
    def init(cls, values: dict) -> dict:
        try:
            config = VectorStoreSettings(**values["config"])
        except Exception as e:
            LOG.error(f"Invalid config: {e}")
            raise ValueError(f"Invalid config: {e}")
        return config

    @abstractmethod
    def connect(*args, **kwargs) -> bool:
        ...

    # Collections

    @abstractmethod
    def list_collections(*args, **kwargs) -> list[Collection]:
        ...

    @abstractmethod
    def get_collection(collection_id: int, *args, **kwargs) -> Collection:
        ...

    @abstractmethod
    def get_collection_by_name(collection_name: str, *args, **kwargs) -> Collection:
        ...

    @abstractmethod
    def create_collection(collection: CollectionCreate, *args, **kwargs) -> Collection:
        ...

    @abstractmethod
    def update_collection(collection_id: int, collection: Collection) -> Collection:
        ...

    @abstractmethod
    def delete_collection(collection_id: int) -> Collection:
        ...

    # Documents

    @abstractmethod
    def list_documents(collection_id: int) -> list[Document]:
        ...

    @abstractmethod
    def list_documents_by_name(collection_name: str) -> list[Document]:
        ...

    @abstractmethod
    def get_document(collection_id: int, document_id: int, *args, **kwargs) -> Document:
        ...
    
    @abstractmethod
    def add_document(collection_id: int, documents: list[DocumentCreate], *args, **kwargs) -> Document:
        ...

    @abstractmethod
    def add_documents(collection_id: int, documents: list[DocumentCreate], *args, **kwargs) -> Document:
        ...

    