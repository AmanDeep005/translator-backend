from fastapi import FastAPI
from .api.routes import app_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Chat App API")

app.include_router(app_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

