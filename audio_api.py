from contextlib import asynccontextmanager
from fastapi import FastAPI, UploadFile
from starlette.responses import Response
from audio_service import AudioService
from temp_file_manager import TempFileManager

audio_service = AudioService()
file_manager = TempFileManager()


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield
    del file_manager


app = FastAPI()


@app.post("/api/text-from-audio")
async def get_text_from_audio(file: UploadFile):
    try:
        content = await file.read()
        filepath = file_manager.save_temp_file(file.filename, content)
    except Exception as ex:
        print(ex)
        return Response(
            content="Возникла ошибка в процессе загрузки файла", status_code=500
        )
    finally:
        await file.close()

    text = audio_service.get_text_from_audio(filepath)
    file_manager.delete_temp_file(file.filename)

    return Response(content=text, status_code=200)
