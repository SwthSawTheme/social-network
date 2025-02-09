from fastapi import APIRouter

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def home():
    return {"status": "ok"}

@router.get("/test")
async def test():
    return {"status": ""}
