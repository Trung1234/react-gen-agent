# backend/graph/state.py
from typing import TypedDict, List, Optional, Annotated
import operator

class AgentState(TypedDict):
    input_prompt: str                     
    visual_context: dict                  
    messages: Annotated[List[str], operator.add] 
    
    react_code: Optional[str]             # Kết quả 1: Code React
    playwright_test_code: Optional[str]   # Kết quả 2: Code Test (MỚI)