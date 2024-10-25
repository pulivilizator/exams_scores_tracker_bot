from pathlib import Path

from environs import Env
from pydantic import BaseModel

from .models import RedisConfig, BotConfig, Database

BASE_DIR = Path(__file__).parent.parent.parent

class ConfigModel(BaseModel):
    redis: RedisConfig
    bot: BotConfig
    db: Database

def get_config(path: str = None) -> ConfigModel:
    env = Env()
    env.read_env(path)

    return ConfigModel(
        redis=RedisConfig(
            dsn='redis://' + env.str('REDIS_STORAGE_DSN'),
        ),
        bot=BotConfig(
            token=env.str('BOT_TOKEN'),
        ),
        db=Database(
            dsn=env.str('POSTGRES_DSN')
        ),
    )