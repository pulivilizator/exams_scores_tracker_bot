from pydantic import BaseModel, RedisDsn, PostgresDsn


class RedisConfig(BaseModel):
    dsn: RedisDsn

class Database(BaseModel):
    dsn: PostgresDsn

class BotConfig(BaseModel):
    token: str
