from fastapi import APIRouter, status
from pydantic import BaseModel
from db import connection

router = APIRouter()

# Data Model
class Chroma(BaseModel):
    name: str

class ChromaEdit(BaseModel):
    name: str
    old_name: str

@router.post("/collection/create/")
async def create_db(item:Chroma):
    print("test>>")
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

