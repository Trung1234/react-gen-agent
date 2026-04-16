# backend/graph/workflow.py
from langgraph.graph import StateGraph, END
from .state import AgentState
from . import nodes

def create_graph():
    workflow = StateGraph(AgentState)

    # --- 1. KHAI BÁO CÁC NODE ---
    workflow.add_node("intent_agent", nodes.intent_node)
    workflow.add_node("code_agent", nodes.code_node)
    workflow.add_node("test_agent", nodes.test_agent)

    # --- 2. ĐIỂM BẮT ĐẦU ---
    workflow.set_entry_point("intent_agent")

    # --- 3. LUỒNG TUYẾN TÍNH (LINEAR FLOW) ---
    # Không có điều kiện, không có vòng lặp (Loop) nữa
    # Chạy theo thứ tự: Phân tích -> Viết Code -> Viết Test -> Kết thúc
    
    workflow.add_edge("intent_agent", "code_agent")
    workflow.add_edge("code_agent", "test_agent")
    workflow.add_edge("test_agent", END)

    # --- 4. BIÊN DỊCH ---
    app = workflow.compile()
    return app