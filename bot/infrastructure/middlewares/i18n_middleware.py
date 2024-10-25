from typing import Callable, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import User, TelegramObject
from dishka.integrations.aiogram import FromDishka
from fluentogram import TranslatorHub

from bot.core import dto
from bot.core.enums import Language, LanguageList
from bot.repository.implementations.user_cache_repository import UserCacheRepository
from .inject_middleware import aiogram_middleware_inject
from ...services.user_service import UserService


class TranslatorRunnerMiddleware(BaseMiddleware):
    @aiogram_middleware_inject
    async def __call__(
            self,
            handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: dict[str, Any],
            hub: FromDishka[TranslatorHub],
            repository: FromDishka[UserCacheRepository],
            user_service: FromDishka[UserService],
    ) -> Any:
        user: User = data.get('event_from_user')

        if user is None:
            return await handler(event, data)

        lang = await self._get_lang(event, user, repository, user_service)
        data['i18n'] = hub.get_translator_by_locale(lang)
        return await handler(event, data)

    @staticmethod
    async def _get_lang(event: TelegramObject, user: User, repository: UserCacheRepository, user_service: UserService) -> str:
        current_lang: dto.UserLanguage = await repository.hget_all(user_id=user.id, response_model=dto.UserLanguage)
        if event.callback_query and Language.WIDGET_KEY in event.callback_query.data:
            new_lang = dto.UserLanguage(
                language=LanguageList.EN
                if current_lang.language == LanguageList.RU
                else LanguageList.RU
            )

            await repository.hset(user_id=user.id, model_data=new_lang)
            await user_service.update(lookup_value=user.id, update_data=new_lang)
            return new_lang.language
        return current_lang.language