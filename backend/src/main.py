from fastapi import FastAPI
from src.controller import convert_controller

app = FastAPI()

app.include_router(convert_controller.router)

@app.get("/")
def read_root():
    return {"message": "API de conversão  funcionando!"}
