from fastapi import APIRouter, HTTPException

from services.collections import CollectionManager
from schemas.collection import Collection, CollectionCreate
from schemas.document import Document, DocumentCreate, DocumentUpdate


router = APIRouter()


@router.get("/collections", response_model=list[Collection], tags=["Collections"])
def list_collections():
    return []


@router.post("/collections/{collection_id}", response_model=Collection, tags=["Collections"])
def get_collection(collection_id: int):
    collection = CollectionManager.get_collection(collection_id)
    return collection


@router.post("/collections", response_model=Collection, tags=["Collections"])
def create_collection(collection: CollectionCreate):
    new_collection = CollectionManager.create_collection(collection)
    return new_collection


@router.put("/collections/{collection_id}", response_model=Collection, tags=["Collections"])
def update_collection(collection_id: int, collection: CollectionUpdate):
    # Replace with actual database update logic
    raise 


@router.delete("/collections/{collection_id}", tags=["Collections"])
def delete_collection(collection_id: int):
    # Replace with actual database deletion logic
    return {"message": f"Collection {collection_id} deleted successfully"}


# Document CRUD Endpoints

@router.get("/documents", response_model=list[Document], tags=["Documents"])
def list_documents():
    # Replace with actual database fetching logic
    return []


@router.get("/documents/{document_id}", response_model=Document, tags=["Documents"])
def get_document(document_id: int):
    # Replace with actual database fetching logic
    if document_id != 1:
        raise HTTPException(status_code=404, detail="Document not found")
    return Document(id=document_id, collection_id=1, content="Sample Content")


@router.post("/documents", response_model=Document, tags=["Documents"])
def create_document(document: DocumentCreate):
    # Replace with actual database creation logic
    return Document(id=1, collection_id=document.collection_id, content=document.content)


@router.put("/documents/{document_id}", response_model=Document, tags=["Documents"])
def update_document(document_id: int, document: DocumentUpdate):
    # Replace with actual database update logic
    return Document(id=document_id, collection_id=1, content=document.content)


@router.delete("/documents/{document_id}", tags=["Documents"])
def delete_document(document_id: int):
    # Replace with actual database deletion logic
    return {"message": f"Document {document_id} deleted successfully"}