from fastapi import FastAPI
from backend.src.home.infrastructure.routes import router as HomeRoutes
from backend.config.services.router_service import router as ApiRoutesProvider


app = FastAPI()

app.include_router(HomeRoutes, tags=["home"])

app.include_router(
    ApiRoutesProvider,
    prefix="/api",
    tags=["api"],
    # dependencies=[Depends(get_token_header)],
)
# 