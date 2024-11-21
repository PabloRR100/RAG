from fastapi import APIRouter, HTTPException

from packages.rag_aas.src.rag_aas.schemas import document
from services.manager import Manager
from schemas.collection import Collection, CollectionCreate
from schemas.document import Document, DocumentAdd, DocumentCreate, DocumentUpdate


class Router:

    def __init__(self, manager: Manager):
        self.router = APIRouter()
        self.manager= manager

    def build(self) -> APIRouter:
        self.router.get("/collections", response_model=list[Collection], tags=["Collections"])(self.list_collections)
        self.router.post("/collections/{collection_id}", response_model=Collection, tags=["Collections"])(self.get_collection)
        self.router.post("/collections", response_model=Collection, tags=["Collections"])(self.create_collection)
        self.router.put("/collections/{collection_id}", response_model=Collection, tags=["Collections"])(self.update_collection)
        self.router.delete("/collections/{collection_id}", tags=["Collections"])(self.delete_collection)

        self.router.get("/collections/{collection_id}/documents", response_model=list[Document], tags=["Documents"])(self.list_documents)
        self.router.get("/collections/{collection_id}/documents/{document_id}", response_model=Document, tags=["Documents"])(self.get_document)
        self.router.post("/collections/{collection_id}/documents/create", response_model=Document, tags=["Documents"])(self.create_document)
        self.router.put("/documents/{document_id}", response_model=Document, tags=["Documents"])(self.update_document)
        self.router.delete("/documents/{document_id}", tags=["Documents"])(self.delete_document)

        return self.router
    

@router.get("/collections", response_model=list[Collection], tags=["Collections"])
def list_collections():
    collections = Manager.list_collections()
    return collections


@router.post("/collections/{collection_id}", response_model=Collection, tags=["Collections"])
def get_collection(collection_id: int):
    collection = Manager.get_collection(collection_id)
    return collection


@router.post("/collections", response_model=Collection, tags=["Collections"])
def create_collection(collection: CollectionCreate):
    new_collection = Manager.create_collection(collection)
    return new_collection


@router.put("/collections/{collection_id}", response_model=Collection, tags=["Collections"])
def update_collection(collection_id: int, collection: Collection):
    # Replace with actual database update logic
    raise NotImplementedError


@router.delete("/collections/{collection_id}", tags=["Collections"])
def delete_collection(collection_id: int):
    # Replace with actual database deletion logic
    deleted_collection = Manager.delete_collection(collection_id)
    return {"message": f"Collection {deleted_collection.id} deleted successfully"}


# Document CRUD Endpoints

@router.get("collections/{collection_id}/documents/", response_model=list[Document], tags=["Documents"])
def list_documents() -> list[Document]:
    # Replace with actual database fetching logic
    return []


@router.get("collections/{collection_id}/documents/{document_id}", response_model=Document, tags=["Documents"])
def get_document(collection_id: str, document_id: int):
    # Replace with actual database fetching logic
    document = Manager.get_document(collection_id, document_id)
    return document


@router.post("collections/{collection_id}/documents/create", response_model=Document, tags=["Documents"])
def create_document(document: DocumentCreate):
    # Replace with actual database creation logic
    new_document = Manager.


@router.post("/documents", response_model=Document, tags=["Documents"])



@router.put("/documents/{document_id}", response_model=Document, tags=["Documents"])
def update_document(document_id: int, document: DocumentUpdate):
    # Replace with actual database update logic
    return Document(id=document_id, collection_id=1, content=document.content)


@router.delete("/documents/{document_id}", tags=["Documents"])
def delete_document(document_id: int):
    # Replace with actual database deletion logic
    return {"message": f"Document {document_id} deleted successfully"}