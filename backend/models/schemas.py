# backend/models/schemas.py
from pydantic import BaseModel
from typing import Dict, Any, Optional, List

class GenerateRequest(BaseModel):
    prompt: str                  
    visual_context: Dict[str, Any] 

class GenerateResponse(BaseModel):
    status: str                  
    code: Optional[str]          
    logs: List[str]              
    error_message: Optional[str] = None