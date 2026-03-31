# backend/models/schemas.py
from pydantic import BaseModel, Dict, Any
from typing import Optional, List

class GenerateRequest(BaseModel):
    prompt: str                  # Lệnh text ví dụ: "Tạo nút đăng nhập màu xanh"
    visual_context: Dict[str, Any] # JSON mô tả layout từ Canvas Frontend

class GenerateResponse(BaseModel):
    status: str                  # "success" hoặc "error"
    code: Optional[str]          # Đoạn code React sinh ra
    logs: List[str]              # Các bước log để debug
    error_message: Optional[str] = None