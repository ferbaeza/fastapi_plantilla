from fastapi import APIRouter
from backend.src.shared.utils.api_response import ApiResponse

router = APIRouter()
name = 'items'

items = [
    {"id":"1", "description": "item_id 1"},
    {"id":"2", "description": "item_id 2"},
    {"id":"3", "description": "item_id 3"},
    {"id":"4", "description": "item_id 4"},
]

@router.get("/items/", name='Get Items Collection')
async def get_items():
    return ApiResponse.json({"items":items}, name)


@router.get("/item/{item_id}", name='Get Item Entity by Id')
async def get_item(item_id: int):
    try:
        return ApiResponse.json({"item_id":items[item_id-1]}, name)
    except:
        response = ApiResponse.error({"data":"item_id Not found"})
        return response

