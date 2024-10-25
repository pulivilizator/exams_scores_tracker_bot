from dishka import Provider, provide, Scope
from redis.asyncio import Redis
from sqlalchemy.ext.asyncio import AsyncSession

from bot.core import dto
from bot.repository.implementations.score_repository import ScoreRepository
from bot.repository.implementations.user_cache_repository import UserCacheRepository
from bot.repository.implementations.user_repository import UserRepository
from bot.repository.models import User, Score


class RepositoryProvider(Provider):

    @provide(scope=Scope.APP)
    def get_cache(self, r: Redis) -> UserCacheRepository:
        return UserCacheRepository(r=r)

    @provide(scope=Scope.REQUEST)
    def get_user_repository(self, session: AsyncSession) -> UserRepository:
        return UserRepository(
            session=session,
            model=User,
            dto_model=dto.User,
            lookup_field='user_id'
        )

    @provide(scope=Scope.REQUEST)
    def get_score_repository(self, session: AsyncSession) -> ScoreRepository:
        return ScoreRepository(
            session=session,
            model=Score,
            dto_model=dto.Score,
            lookup_field='score_id'
        )








