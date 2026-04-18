import os
from dotenv import load_dotenv

# Load biến môi trường từ .env (chỉ dùng khi chạy local)
load_dotenv()

class Settings:
    # Ưu tiên lấy từ biến môi trường trên Azure
    # Nếu không có thì fallback về localhost (chỉ dùng khi develop local)
    BACKEND_URL = os.getenv(
        "BACKEND_URL", 
        "http://localhost:8000"
    )

settings = Settings()