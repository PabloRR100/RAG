import logging

from rag_aas.schemas.collection import Collection
from rag_aas.schemas.config import VectorStoreSettings
from rag_aas.schemas.document import Document
from rag_aas.services.manager import Manager
from rag_aas.services.pgvector.config import PGVectorStoreSettings
from rag_aas.services.pgvector.vectorstore import PGVectorStore


LOG = logging.getLogger(__name__)


class PGVectorManager(Manager):
    """
    Manager for the PG Vector Store.
    """

    def __init__(
        self, 
        vector_store: PGVectorStore = None,
        vector_store_settings: PGVectorStoreSettings | None = None,
    ):
        LOG.info("Loading Vector Store")
        if not vector_store_settings:
            vector_store_settings: PGVectorStoreSettings = VectorStoreSettings()
        if vector_store is None:
            vector_store = PGVectorStore(
                connection=vector_store_settings.connection
            )
        self.vector_store= vector_store

    # Collections 
    # --

    def list_collections(self) -> list[Collection]:
        return self.vector_store.list_collections()
    
    def get_collection(self, collection_id: int) -> Collection:
        return self.vector_store.get_collection(collection_id)
    
    def get_collection_by_name(self, collection_name: str) -> Collection:
        return self.vector_store.get_collection_by_name(collection_name)
    
    def create_collection(self, collection: Collection) -> Collection:
        return self.vector_store.create_collection(collection)
    
    def update_collection(self, collection_id: int, collection: Collection) -> Collection:
        return self.vector_store.update_collection(collection_id, collection)
    
    def delete_collection(self, collection_id: int) -> Collection:
        return self.vector_store.delete_collection(collection_id)
    
    def list_documents(self, collection_id: int) -> list[Document]:
        return self.vector_store.list_documents(collection_id)
    
    # Documents
    # --

    def get_document(self, collection_id: int, document_id: int) -> Document:
        return self.vector_store.get_document(collection_id, document_id)
    
    def get_document_by_name(self, collection_name: str, document_name: str) -> Document:
        return self.vector_store.get_document_by_name(collection_name, document_name)
    
    def add_documents(self, collection_id: int, documents: list[Document]) -> Document:
        return self.vector_store.add_documents(collection_id, documents)
    
    def delete_document(self, collection_id: int, document_id: int) -> Document:
        return self.vector_store.delete_document(collection_id, document_id)
    
    def delete_document_by_name(self, collection_name: str, document_name: str) -> Document:
        return self.vector_store.delete_document_by_name(collection_name, document_name)
    
    def update_document(self, collection_id: int, document_id: int, document: Document) -> Document:
        return self.vector_store.update_document(collection_id, document_id, document)
    

