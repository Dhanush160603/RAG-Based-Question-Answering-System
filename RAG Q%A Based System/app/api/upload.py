from fastapi import APIRouter, UploadFile, File, BackgroundTasks
import os
from app.config import UPLOAD_FOLDER

router = APIRouter()

@router.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks = None
):
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    if not file.filename.endswith((".txt", ".pdf")):
        return {"error": "Only TXT and PDF files allowed"}

    path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(path, "wb") as f:
        f.write(await file.read())

    return {"message": "File uploaded successfully", "filename": file.filename}
