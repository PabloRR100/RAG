from rag_aas.schemas.config import VectorStoreSettings


class PGVectorStoreSettings(VectorStoreSettings):
    """
    Settings for the PGVectorStore.
    """
    VECTOR_STORE_TYPE = "pgvector"
    CONNECTION_STRING: str

