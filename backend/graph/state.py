# backend/graph/state.py
from typing import TypedDict, List, Optional, Annotated
import operator

class AgentState(TypedDict):
    input_prompt: str                     # Prompt gốc
    visual_context: dict                  # Dữ liệu visual
    messages: Annotated[List[str], operator.add] # Lịch sử chat
    react_code: Optional[str]             # Code React sinh ra
    syntax_error: Optional[str]           # Lỗi nếu có
    is_valid: bool                        # Trạng thái đã pass validator chưa