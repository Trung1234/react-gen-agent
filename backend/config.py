# backend/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    MODEL_NAME = "gemini-3.1-pro-preview"
    MAX_RETRIES = 3
    TEMPERATURE = 0

settings = Settings()