from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

from api.core.database import engine
from api.core.settings import get_settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        async with engine.connect() as db:
            await db.execute(text("SELECT 1"))

        yield

    finally:
        await engine.dispose()

def create_app() -> FastAPI:
    settings = get_settings()
    is_prod_env = settings.app_env == 'prod'

    app = FastAPI(
        title = settings.app_name,
        version = settings.app_version,
        debug = False,
        lifespan = lifespan,
        docs_url = None if is_prod_env else "/docs",
        redoc_url = None if is_prod_env else "/redoc",
        openapi_url = None if is_prod_env else "/openapi.json",
    )

    return app

app = create_app()
