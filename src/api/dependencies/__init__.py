from collections.abc import AsyncGenerator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.core.database import SessionFactory


async def get_db_session() -> AsyncGenerator[AsyncSession]:
    async with SessionFactory() as session:
        yield session

DbSessionDep = Annotated[AsyncSession , Depends(get_db_session)]
