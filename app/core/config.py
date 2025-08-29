import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = "sqlite:///./workout.db"  # SQLite local

settings = Settings()