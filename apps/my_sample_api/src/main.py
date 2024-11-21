from rag_aas.api.builder import APIBuilder
from rag_aas.services.manager import Manager


class CustomManager(Manager):
    ...


builder = APIBuilder(
    manager=CustomManager(),
)






