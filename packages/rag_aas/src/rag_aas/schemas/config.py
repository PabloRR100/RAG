import logging
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()
LOG = logging.getLogger(__name__)


class VectorStoreSettings(BaseSettings):
    """
    Settings for the RAG AAS.
    """
    VECTOR_STORE_TYPE: str

