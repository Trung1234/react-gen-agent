from langgraph.graph import StateGraph, END
from .state import AgentState
from . import nodes

def create_graph():
    workflow = StateGraph(AgentState)

    # --- 1. KHAI BÁO CÁC NODE ---
    workflow.add_node("intent_agent", nodes.intent_node)      # Phân tích ý định (Bắt buộc)
    workflow.add_node("code_agent", nodes.code_node)          # Viết code
    workflow.add_node("validator_agent", nodes.validator_node)# Kiểm thử (Selenium)
    workflow.add_node("exception_agent", nodes.exception_node)# Xử lý lỗi (Sửa lỗi)

    # --- 2. ĐIỂM BẮT ĐẦU ---
    # Bắt đầu từ Intent để hiểu ý đồ User trước
    workflow.set_entry_point("intent_agent")

    # --- 3. LUỒNG CHÍNH (LINEAR FLOW) ---
    workflow.add_edge("intent_agent", "code_agent")
    workflow.add_edge("code_agent", "validator_agent")

    # --- 4. ĐIỀU KIỆN (CONDITIONAL EDGE) ---
    def check_validation_result(state: AgentState):
        # Kiểm tra cờ is_valid do Validator Agent set
        if state["is_valid"]:
            return "end"
        else:
            return "retry"  # Nếu sai, đi vào luồng sửa lỗi

    workflow.add_conditional_edges(
        "validator_agent",
        check_validation_result,
        {
            "end": END,              # Hợp lệ -> Kết thúc
            "retry": "exception_agent" # Lỗi -> Qua Exception Agent
        }
    )

    # --- 5. LUỒNG SỬA LỖI (LOOP BACK) ---
    # Exception Agent xử lý xong -> Quay lại Code Agent viết lại
    workflow.add_edge("exception_agent", "code_agent")

    # --- 6. BIÊN DỊCH ---
    app = workflow.compile()
    return app