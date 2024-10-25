from dishka import Provider, provide, Scope

from bot.repository.implementations.user_repository import UserRepository
from bot.services.user_service import UserService


class ServiceProvider(Provider):
    @provide(scope=Scope.REQUEST)
    def get_user_service(self, repository: UserRepository) -> UserService:
        return UserService(repository=repository)