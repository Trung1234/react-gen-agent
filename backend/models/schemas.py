# backend/models/schemas.py
from pydantic import BaseModel
from typing import Dict, Any, Optional, List

class GenerateRequest(BaseModel):
    prompt: str                  
    visual_context: dict 

class GenerateResponse(BaseModel):
    status: str                  
    react_code: Optional[str] = None           # <-- Thêm dòng này
    playwright_test_code: Optional[str] = None # <-- Thêm dòng này
    logs: List[str] = []                       # Logs