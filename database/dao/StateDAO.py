import asyncio
from typing import List, Optional

from sqlalchemy.ext.asyncio import AsyncSession

from database.dao.BaseDAO import BaseDAO
from database.models.state import State
from schemas.state import StateSchema


class StateDAO(BaseDAO):
    def __init__(self, session: AsyncSession):
        super().__init__(session, State, StateSchema)

    async def add(self, state: StateSchema) -> None:
        lock = asyncio.Lock()
        async with lock:
            await self._create(state)

    async def delete(self, state_id: int) -> None:
        lock = asyncio.Lock()
        async with lock:
            await self._delete(state_id)

    async def get(self, state_id: int) -> Optional[State]:
        return await self._get(state_id)

    async def update(self, state_id: int, **kwargs) -> Optional[State]:
        lock = asyncio.Lock()
        async with lock:
            return await self._update(state_id, **kwargs)

    async def list(self, **kwargs) -> Optional[List[State]]:
        return await self._list(**kwargs)

    async def delete_all(self) -> None:
        lock = asyncio.Lock()
        async with lock:
            await self._delete_all()
