from fastapi import APIRouter
from .endpoints import amit_function,duhan
app_router = APIRouter() 



app_router.get("/amit")(amit_function)
app_router.post("/translator")(duhan)