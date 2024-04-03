from fastapi import APIRouter, status,  File, UploadFile
from pydantic import BaseModel, HttpUrl
from db import connection
import shutil
from rag import ingest 
from rag import query
from rag import web_scraper
from config import constants
SOURCE_DOCUMENTS  = constants.source_directory

router = APIRouter()
class Collection(BaseModel):
    name: str

class CollectionQuery(BaseModel):
    collection_name: str
    query: str


class Scrapper(BaseModel):
    url: HttpUrl
    query: str

@router.post("/rag/embed/")
async def embed(collection:str, file: UploadFile = File(...)):
    with open(f"{SOURCE_DOCUMENTS}/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"message": ingest.main(collection)}


@router.post("/rag/query/")
async def embed(collection:CollectionQuery):
    return query.main(collection)


@router.post("/rag/scrapper/")
async def scrapper(collection:Scrapper):
    return web_scraper.main(collection.url, collection.query)
    