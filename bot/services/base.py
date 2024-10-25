from abc import ABC, abstractmethod
from typing import TypeVar, Optional, Type, Any

from pydantic import BaseModel

from bot.repository.interfaces.base import AbstractSQLRepository

DTOModel = TypeVar('DTOModel', bound=BaseModel)

class AbstractService(ABC):
    @abstractmethod
    def create(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def retrieve(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def exists(self, *args, **kwargs):
        raise NotImplementedError


class BaseSQLService(AbstractService):
    def __init__(self, repository: AbstractSQLRepository):
        self._repository = repository

    async def create(self, data: BaseModel,
                     response_model: Optional[Type[DTOModel]] = None):
        return await self._repository.create(data, response_model)

    async def retrieve(self,
                       lookup_value: Any,
                       response_model: Optional[Type[DTOModel]] = None,
                       raise_for_none=True,
                       instance_returned=False
                       ):
        return await self._repository.retrieve(
                lookup_value=lookup_value,
                response_model=response_model,
                raise_for_none = raise_for_none,
                instance_returned = instance_returned
        )

    async def update(self, lookup_value,
                     update_data: BaseModel,
                     response_model: Optional[Type[DTOModel]] = None):
        return await self._repository.update(lookup_value, update_data, response_model)

    async def exists(self, lookup_value: Any) -> bool:
        return await self._repository.retrieve(lookup_value, raise_for_none=False) is not None