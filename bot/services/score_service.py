from sqlalchemy import select

from bot.repository.models import Score
from bot.services.base import BaseSQLService


class ScoreService(BaseSQLService):
    async def list(self, user_id):
        query = select(Score).where(Score.user_id == user_id)
        return await self._repository.list(query)

    async def delete(self, obj_id):
        await self._repository.destroy(obj_id)