from fastapi import APIRouter


from services.collections import CollectionManager
from schemas.collection import Collection, CollectionCreate


router = APIRouter()


@router.get("/collections", response_model=list[Collection], tags=["Collections"])
def list_collections():
    return []


@router.post("/collections/{collection_id}", response_model=Collection, tags=["Collections"])
def get_collection(collection_id: int):
    return Collection(id=collection_id, name="Collection Name")


@router.post("/collections", response_model=Collection, tags=["Collections"])
def create_collection(collection: CollectionCreate):
    return collection

