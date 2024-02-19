from fastapi import APIRouter
from .home_controller import HomeController

router = APIRouter()

@router.get("/", name='Home')
async def get_items():
    return await HomeController.get_home()
