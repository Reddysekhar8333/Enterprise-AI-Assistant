import os
from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

router = APIRouter()

UPLOAD_DIR = "documents"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "filename": file.filename,
        "path": file_path
    }