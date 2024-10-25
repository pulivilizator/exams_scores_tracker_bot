from dishka import Provider

from .base_provider import BaseProvider
from .i18n_provider import I18nProvider
from .repository_providers import RepositoryProvider
from .service_provider import ServiceProvider


def get_providers() -> list[Provider]:
    return [
        BaseProvider(),
        RepositoryProvider(),
        I18nProvider(),
        ServiceProvider(),
    ]