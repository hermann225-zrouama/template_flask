from dotenv import load_dotenv
load_dotenv("./.env")
from fastapi import FastAPI
from app.models import entreprises
from app.models import commerciaux
from app.config.db import engine
from app.routes.global_router import router

app = FastAPI()

# DB init
entreprises.Base.metadata.create_all(bind=engine)
commerciaux.Base.metadata.create_all(bind=engine)

# Router
app.include_router(router, prefix="", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Hello World"}
