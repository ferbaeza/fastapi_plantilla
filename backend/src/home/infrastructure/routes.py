from fastapi import APIRouter, Depends
from typing import Annotated
from .home_controller import HomeController

router = APIRouter()

@router.get("/", name='Home')
async def get_items(data : dict = Depends(HomeController.get_home)):
    return data
    # return await HomeController.get_home()
