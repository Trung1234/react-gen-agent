# backend/graph/state.py
from typing import TypedDict, List, Optional, Annotated
import operator

class AgentState(TypedDict):
    input_prompt: str                     
    visual_context: dict                  
    messages: Annotated[List[str], operator.add] # Lịch sử chat
    react_code: Optional[str]             # Code hiện tại
    preview_image_base64: Optional[str]   # Ảnh chụp từ Selenium
    is_valid: bool                        # Code đã pass kiểm tra chưa?
    error_log: Optional[str]              # Thông báo lỗi cụ thể (để Exception Agent đọc)