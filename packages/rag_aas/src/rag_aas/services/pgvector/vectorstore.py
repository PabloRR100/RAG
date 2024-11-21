import logging

from langchain_core.documents import Document
# from langchain_core.embeddings import Embeddings
from langchain_postgres import PGVector

from rag_aas.schemas.collection import Collection


LOG = logging.getLogger(__name__)


class PGVectorStore(PGVector):
    """
    Extension over PGVector to provide additional functionality.
    """

    # Collections 
    # --

    def _to_collection(collection: dict) -> Collection:
        return Collection(
            id=collection["id"],
            name=collection["name"],
            description=collection["description"]
        )
    
    def _update_collection(self, collection_id: int = None, collection_name: str = None):
        """Updates the collection in the PGVector state"""
        if not collection_id and not collection_name:
            raise ValueError("Either collection_id or collection_name must be provided")
        if collection_id:
            collection = self.get_collection(collection_id)
            collection_name = collection.name
        self.collection_name = collection_name
        LOG.debug(f"Collection updated to {collection_name}")

    def list_collections(self) -> list[Collection]:
        with self.vector_store as conn:
            collections = conn.execute(
                """
                SELECT * FROM collections;
                """
            )
            return [self._to_collection(collection) for collection in collections]
        
    def get_collection(self, collection_id: int) -> Collection:
        """
        Overrides the get_collection method to return a Collection object and retrieve by id.
        The default implementation returns a dictionary and is retrieved by name, which is not even passed. 
        PGVectorStore can deal with a single collection keeping it in a internal state.
        """
        with self.vector_store as conn:
            collection = conn.execute(
                """
                SELECT * FROM collections WHERE id = %s;
                """,
                (collection_id,)
            ).fetchone()
            return self._to_collection(collection)
    
    def get_collection_by_name(self, collection_name: str) -> Collection:
        with self.vector_store as conn:
            collection = conn.execute(
                """
                SELECT * FROM collections WHERE name = %s;
                """,
                (collection_name,)
            ).fetchone()
            return self._to_collection(collection)
        
    def create_collection(self, collection: Collection) -> Collection:
        self.collection_name = collection.name
        return super().create_collection()
    
    def update_collection(self, collection_id: int, collection: Collection) -> Collection:
        raise NotImplementedError
    
    def delete_collection(self, collection_id: int) -> Collection:
        collection = self.get_collection(collection_id)
        self.delete_collection_by_name(collection.name)
        return 

    def delete_collection_by_name(self, collection_name: str) -> Collection:
        self._update_collection(collection_name=collection_name)
        super().delete_collection()

    
    # Documents
    # --

    def list_documents(self, collection_id: int, filters: list[dict] = None) -> list[Document]:
        # self._update_collection(collection_id=collection_id)
        if filters:
            raise NotImplementedError("Filters are not implemented yet")
        with self.vector_store as conn:
            documents = conn.execute(
                """
                SELECT * FROM documents WHERE collection_id = %s;
                """,
                (collection_id,)
            )
            return [Document(id=document["id"], content=document["content"]) for document in documents]
    
    def get_document(self, collection_id: int, document_id: int) -> Document:
        with self.vector_store as conn:
            document = conn.execute(
                """
                SELECT * FROM documents WHERE collection_id = %s AND id = %s;
                """,
                (collection_id, document_id)
            ).fetchone()
            return Document(id=document["id"], content=document["content"])
    
    def get_document_by_name(self, collection_name: str, document_id: int) -> Document:
        collection = self.get_collection_by_name(collection_name)
        return self.get_document(collection.id, document_id)
    
    def add_documents(self, collection_id: int, documents: list[Document]) -> Document:
        self._update_collection(collection_id=collection_id)
        return super().add_documents(documents)
    
    def add_embeddings(self, texts, embeddings, metadatas = None, ids = None, **kwargs) -> list[str]:
        return super().add_embeddings(texts, embeddings, metadatas, ids, **kwargs)
    
    def delete_document(self, collection_id: int, document_id: int) -> Document:
        self._update_collection(collection_id=collection_id)
        return super().delete_document(document_id)
    
    def delete_document_by_name(self, collection_name: str, document_name: str) -> Document:
        collection = self.get_collection_by_name(collection_name)
        return self.delete_document(collection.id, document_name)   
