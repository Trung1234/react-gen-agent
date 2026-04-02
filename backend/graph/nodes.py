# backend/graph/nodes.py
from .state import AgentState
from services.llm_service import get_llm

# Lấy instance LLM
llm = get_llm()

def intent_node(state: AgentState):
    """Agent 1: Phân tích ý định từ prompt và visual context"""
    print("🤖 [Intent Node] Đang phân tích yêu cầu...")
    
    prompt = f"""
    Yêu cầu: {state['input_prompt']}
    Dữ liệu giao diện: {state['visual_context']}
    
    Nhiệm vụ: Phân tích và tóm tắt cấu trúc UI cần thiết.
    """
    response = llm.invoke(prompt)
    return {"messages": [f"Intent Analysis: {response.content}"]}

def code_node(state: AgentState):
    """Agent 2: Sinh code React"""
    print("👨‍💻 [Code Node] Đang viết code React...")
    
    # Xây dựng prompt
    system_prompt = "Bạn là chuyên gia Frontend React và Tailwind CSS. Viết code sạch, đúng syntax."
    
    # Nếu có lỗi từ vòng lặp trước, yêu cầu sửa
    if state.get("syntax_error"):
        system_prompt += f"\n⚠️ LỖI PHÁT HIỆN: {state['syntax_error']}\nHãy viết lại code để sửa lỗi này."

    user_request = state['messages'][-1] if state['messages'] else state['input_prompt']
    
    full_prompt = f"{system_prompt}\nYêu cầu chi tiết: {user_request}\nVisual Data: {state['visual_context']}"
    
    response = llm.invoke(full_prompt)
    
    return {
        "react_code": response.content,
        "syntax_error": None  # Reset lỗi khi thử lại
    }

def validator_node(state: AgentState):
    """Agent 3: Kiểm tra tính hợp lệ (Syntax cơ bản)"""
    print("✅ [Validator Node] Đang kiểm tra code...")
    
    code = state.get("react_code", "")
    
    # Logic kiểm tra đơn giản (có thể nâng cấp bằng AST checker)
    if not code or len(code) < 50:
        return {"is_valid": False, "syntax_error": "Code quá ngắn hoặc bị lỗi trống."}
    
    if "export default" not in code and "function " not in code:
        return {"is_valid": False, "syntax_error": "Thiếu khai báo component hoặc export."}

    # Giả lập pass
    return {"is_valid": True}