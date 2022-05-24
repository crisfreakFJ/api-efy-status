import os
from pydantic import BaseSettings
from dotenv import load_dotenv
load_dotenv()

class Settings(BaseSettings):
    api_key: str = os.getenv('API_KEY')