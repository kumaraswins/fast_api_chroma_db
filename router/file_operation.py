from fastapi import APIRouter,  File, UploadFile
import shutil

SOURCE_DOCUMENTS  = "source_documents"
router = APIRouter()

@router.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    with open(f"{SOURCE_DOCUMENTS}/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename,"message":f"file saved in {SOURCE_DOCUMENTS}/{file.filename}"}