from fastapi import APIRouter
from backend.src.shared.utils.api_response import ApiResponse


router = APIRouter()
name="api"

@router.get("/", name=name)
async def read_root():
    return ApiResponse.json({"coder":"Hello World"}, name)
