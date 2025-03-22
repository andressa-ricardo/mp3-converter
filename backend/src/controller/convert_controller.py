from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import FileResponse
import os
from src.service.convert_service import video_to_audio

router = APIRouter()

@router.post("/convert")
async def convert_video(file: UploadFile = File()):
    temp_video_path = f"temp_{file.filename}"
    
    try:
        with open(temp_video_path, "wb") as buffer:
            buffer.write(file.file.read())

        output_folder = "output"
        audio_path = video_to_audio(temp_video_path, output_folder)

        return FileResponse(audio_path, media_type="audio/mpeg", filename=os.path.basename(audio_path))
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro na conversão: {str(e)}")
    
    finally:
        if os.path.exists(temp_video_path):
            os.remove(temp_video_path)
