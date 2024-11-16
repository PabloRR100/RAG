from abc import ABC, abstractmethod

from schemas.collection import Collection, CollectionCreate


class CollectionManager(ABC):
    """
    Abstract class for managing collections.
    """

    @abstractmethod
    def list_collections() -> list[Collection]:
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
    
