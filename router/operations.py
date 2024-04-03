from fastapi import APIRouter, status
from pydantic import BaseModel
from db import connection
from text_formatter import txt_format

router = APIRouter()

# Data Model
class Chroma(BaseModel):
    name: str

class ChromaEdit(BaseModel):
    name: str
    old_name: str

class CollectionTxt(BaseModel):
    file_name:str
    collection_name:str


class Collection(BaseModel):
    collection_name:str
    query:str


@router.post("/collection/create/")
async def create_db(item:Chroma):
    return {"data":connection.create_collection(item.name)}


@router.post("/collection/edit")
async def edit_collelction(item: ChromaEdit):
    return {"data":connection.edit_collection(item.old_name, item.name)}


@router.get("/collection/count")
async def list_all_collection():
    return {"data": connection.list_all_collection(),"count":connection.count_collection()}


@router.get("/collection/delete")
async def delete_collection(item:Chroma):
    return {"data": connection.delete_collection(item.name)}



@router.post("/add/collection/txt")
async def add_txt_to_collection(item:CollectionTxt):
    """
    1. create collection
    2. get the doc splittings
    """
    docs = txt_format.get_raw_text_doc(item.file_name)
    collection = connection.create_collection(item.collection_name)
    collection.add(
        documents=docs['docs'],
        metadatas=docs['meta'],
        ids=docs['id']
        
    )
    return {"data": "added to the collection"}

@router.post("/query/collection/txt")
async def query_txt_to_collection(item:Collection):
    collection = connection.get_client_ref(item.collection_name)
    results = collection.query(
        query_texts=[item.query],
        n_results=5
    )
    return {"data":results}