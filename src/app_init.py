from fastapi import FastAPI

from src.routers.default_router import app as default_router

app = FastAPI()
app.include_router(default_router)
