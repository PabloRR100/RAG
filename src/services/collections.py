from abc import ABC, abstractmethod


class CollectionManager(ABC):

    @abstractmethod
    def list_collections() -> list:
        ...

    @abstractmethod
    def get_collection(collection_id: int) -> dict:
        ...

    @abstractmethod
    def create_collection(collection: dict) -> dict:
        ...

    @abstractmethod
    def delete_collection(collection_id: int) -> dict:
        ...
    
