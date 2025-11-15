from pydantic_settings import BaseSettings
from pydantic import Field, field_validator

class Config(BaseSettings):
    database_path: str = Field(default='src/plugins/nonebot_plugin_turbobot/database/botKey.db')
    api_base_url: str = Field(default='https://api.sys-allnet.com')
    bot_name: str = Field(default="Turbobot")