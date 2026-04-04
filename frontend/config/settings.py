# frontend/config/settings.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Địa chỉ của Backend đang chạy (localhost:8000)
    BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")

settings = Settings()