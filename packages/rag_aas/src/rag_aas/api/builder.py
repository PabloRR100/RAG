import logging
from fastapi import FastAPI

from rag_aas.api.routers import Router
from services.manager import Manager


LOG = logging.getLogger(__name__)


class APIBuilder:

    @staticmethod
    def build_rag_api(
        router: Router,
        manager: Manager,
    ) -> FastAPI:
        LOG.debug("Building RAG API")
        app = FastAPI()
        app.include_router(router)
        return app


