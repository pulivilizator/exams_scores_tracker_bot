from dishka import Provider, provide, Scope
from fluentogram import TranslatorHub

from bot.infrastructure.utils.i18n import create_translator_hub


class I18nProvider(Provider):

    @provide(scope=Scope.APP)
    def get_translator_hub(self) -> TranslatorHub:
        translator_hub = create_translator_hub()
        return translator_hub





