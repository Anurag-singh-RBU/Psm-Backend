from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    async_sessionmaker,
    create_async_engine,
)

from api.core.settings import get_settings

settings = get_settings()

engine: AsyncEngine = create_async_engine(
    settings.database_url,
    pool_pre_ping = True,
)

session_factory = async_sessionmaker(
    bind = engine,
    expire_on_commit = False,
)
