from fastapi import APIRouter
from backend.src.api.infrastructure import routes as ApiRoutes
from backend.src.items.infrastructure import routes as ItemsRoutes


router = APIRouter()

router.include_router(ApiRoutes.router)

router.include_router(ItemsRoutes.router)