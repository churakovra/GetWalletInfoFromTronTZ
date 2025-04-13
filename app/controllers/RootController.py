from fastapi import APIRouter

root_router = APIRouter()


@root_router.get("/")
async def root_handler():
    return {"response": "Yep, i'm alive"}
