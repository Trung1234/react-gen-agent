# backend/graph/workflow.py
from langgraph.graph import StateGraph, END
from .state import AgentState
from . import nodes

def create_graph():
    # Khởi tạo đồ thị với State đã định nghĩa
    workflow = StateGraph(AgentState)

    # Thêm các node
    workflow.add_node("intent_agent", nodes.intent_node)
    workflow.add_node("code_agent", nodes.code_node)
    workflow.add_node("validator_agent", nodes.validator_node)

    # Định nghĩa điểm bắt đầu
    workflow.set_entry_point("intent_agent")

    # Nối các luồng cố định
    workflow.add_edge("intent_agent", "code_agent")
    workflow.add_edge("code_agent", "validator_agent")

    # Định nghĩa luồng có điều kiện (Nếu lỗi -> quay lại, Nếu đúng -> kết thúc)
    def decide_next_step(state: AgentState):
        if state["is_valid"]:
            return "end"
        else:
            return "retry"

    workflow.add_conditional_edges(
        "validator_agent",
        decide_next_step,
        {
            "retry": "code_agent",  # Quay lại Code Agent để sửa
            "end": END             # Kết thúc luồng
        }
    )

    # Biên dịch
    app = workflow.compile()
    return app