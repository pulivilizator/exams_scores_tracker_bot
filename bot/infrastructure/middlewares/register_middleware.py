from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import User, TelegramObject
from dishka.integrations.aiogram import FromDishka

from bot.core import dto
from bot.core.config.config import ConfigModel
from bot.repository.implementations.user_cache_repository import UserCacheRepository
from .inject_middleware import aiogram_middleware_inject
from ...services.user_service import UserService


class RegisterMiddleware(BaseMiddleware):
    @aiogram_middleware_inject
    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any],
            repository: FromDishka[UserCacheRepository],
            user_service: FromDishka[UserService],
            config: FromDishka[ConfigModel]
    ) -> Any:
        user: User = data.get('event_from_user')

        if user is None:
            return await handler(event, data)


        if not await repository.user_exists(user_id=user.id):
            db_user: dto.User | None = await user_service.retrieve(user.id, raise_for_none=False)
            if db_user is None:
                new_user = dto.UserBase(
                    user_id=user.id,
                    first_name=user.first_name,
                    last_name=user.last_name,
                )
                db_user = await user_service.create(new_user)
            await repository.hset(user_id=user.id, model_data=db_user)




        return await handler(event, data)