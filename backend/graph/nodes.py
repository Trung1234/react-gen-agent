# backend/graph/nodes.py
from .state import AgentState
from services.llm_service import get_llm
from services.selenium_service import take_screenshot_of_react_code

llm = get_llm()

def intent_node(state: AgentState):
    """Agent 1: Phân tích ý định từ prompt và visual context"""
    print("🤖 [Intent Node] Đang phân tích yêu cầu...")
    
    prompt = f"""
    Role: Frontend Architect.
    User Request: {state['input_prompt']}
    Visual Data: {state['visual_context']}
    
    Task: Phân tích yêu cầu và tóm tắt lại cấu trúc UI cần thiết.
    Đừng viết code ngay, hãy chỉ mô tả kỹ thuật (layout, màu sắc, component).
    """
    response = llm.invoke(prompt)
    # Lưu kết quả phân tích vào messages để Code Agent đọc sau này
    return {"messages": [f"Intent Analysis: {response.content}"]}


def code_node(state: AgentState):
    """Code Agent: Sinh code"""
    print("👨‍💻 [Code Agent] Đang sinh code...")
    
    # Nếu có error_log từ Exception Agent trước đó, prompt sẽ tự hiểu để sửa
    context = state['messages'][-1] if state['messages'] else state['input_prompt']
    
    prompt = f"""
    Role: Expert React Developer.
    Task: Write React code based on requirements.
    Requirements: {context}
    Visual Context: {state['visual_context']}
    """
    
    response = llm.invoke(prompt)
    return {
        "react_code": response.content, 
        "is_valid": False, # Reset về false để đi kiểm tra lại
        "preview_image_base64": None # Reset ảnh cũ
    }

def validator_node(state: AgentState):
    """Validator Agent: Kiểm tra Syntax + CHẠY THỰC TẾ (Selenium)"""
    print("✅ [Validator Agent] Đang kiểm thử (Syntax + Selenium)...")
    
    code = state.get("react_code", "")
    
    # 1. Kiểm tra Syntax cơ bản
    if "export default" not in code or len(code) < 50:
        return {
            "is_valid": False, 
            "error_log": "Lỗi cú pháp: Code quá ngắn hoặc thiếu component."
        }
    
    # 2. Chạy Selenium (Visual Test)
    print("   -> Đang chụp ảnh giao diện...")
    img_b64 = take_screenshot_of_react_code(code)
    
    # 3. Đánh giá kết quả Selenium
    # Ở đây đơn giản hóa: Nếu không lấy được ảnh hoặc ảnh bị lỗi thì coi như Fail
    if not img_b64:
        return {
            "is_valid": False, 
            "error_log": "Lỗi Runtime: Code không render được trên trình duyệt (Selenium lỗi)."
        }
    
    # Nếu thành công
    print("   -> Kết quả: PASS")
    return {
        "is_valid": True, 
        "preview_image_base64": img_b64,
        "error_log": None
    }

def exception_node(state: AgentState):
    """Exception Agent: Phân tích lỗi và đưa ra giải pháp sửa chữa"""
    print("🚨 [Exception Agent] Phát hiện lỗi! Đang phân tích nguyên nhân...")
    
    error_msg = state.get("error_log", "Unknown error")
    
    # Prompt để Exception Agent phân tích lỗi
    prompt = f"""
    Role: Senior Debugger.
    The generated React code failed the test with the following error:
    ERROR: {error_msg}
    
    Current Code (partial):
    {state.get('react_code', '')[:200]}...
    
    Analyze the error and explain how to fix it in one sentence.
    """
    
    response = llm.invoke(prompt)
    fix_instruction = response.content
    
    # Cập nhật messages để Code Agent lần sau đọc được hướng dẫn sửa
    return {
        "messages": [f"⚠️ FIX REQUEST: {fix_instruction}"] 
    }