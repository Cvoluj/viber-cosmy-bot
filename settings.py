import json
from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(kw_only=True)
class Settings:
    expose_url: str
    api_token: str
    auth_token: str

    cosmy_api_key: str
    cosmy_api_token: str | None = None

    admin_password: str

    @staticmethod
    def init_settings():
        with open('viber.json', mode='r') as file:
            data = json.load(file)
            expose_url = data.get('url')

        api_token = os.getenv('API_TOKEN')
        auth_token = os.getenv('AUTH_TOKEN')
        cosmy_api_key = os.getenv("COSMY_API_KEY")
        admin_password = os.getenv("ADMIN_PASSWORD")

        if not api_token:
            raise KeyError("API_TOKEN is missing in the .env file.")
        if not auth_token:
            raise KeyError("AUTH_TOKEN is missing in the .env file.")
        if not cosmy_api_key:
            raise KeyError("COMSY_API_KEY is missing in the .env file.")
        if not admin_password:
            raise KeyError("ADMIN_PASSWORD is missing in the .env file.")

        return Settings(
            expose_url=expose_url,
            api_token=api_token,
            auth_token=auth_token,
            cosmy_api_key=cosmy_api_key,
            admin_password=admin_password
        )

settings = Settings.init_settings()
