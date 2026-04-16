# backend/graph/nodes.py
from .state import AgentState
from services.llm_service import get_llm
from utils.file_loader import load_prompt  # <-- Import hàm mới

llm = get_llm()

def intent_node(state: AgentState):
    print("🤖 [Intent Node] Đang phân tích yêu cầu...")
    
    # 1. Load prompt từ file MD
    system_prompt = load_prompt("intent_agent.md")
    
    # 2. Điền biến vào prompt (dùng format)
    full_prompt = system_prompt.format(
        user_request=state['input_prompt'],
        visual_context=state['visual_context']
    )
    
    # 3. Gọi Gemini
    response = llm.invoke(full_prompt)
    
    return {"messages": [f"Intent Analysis: {response.content}"]}

def code_node(state: AgentState):
    print("👨‍💻 [Code Agent] Đang sinh code React...")
    
    # Lấy kết quả phân tích từ Intent Agent
    tech_analysis = state['messages'][-1] if state['messages'] else state['input_prompt']
    
    # 1. Load prompt
    system_prompt = load_prompt("code_agent.md")
    
    # 2. Điền biến
    full_prompt = system_prompt.format(
        tech_analysis=tech_analysis,
        visual_context=state['visual_context'],
        error_log=state.get("error_log", "None") # Truyền lỗi nếu có
    )
    
    response = llm.invoke(full_prompt)
    
    return {
        "react_code": response.content, 
        "error_log": None # Reset lỗi
    }

def test_agent_node(state: AgentState):
    print("🧪 [Test Agent] Đang tạo Playwright Test...")
    
    # 1. Load prompt
    system_prompt = load_prompt("test_agent.md")
    
    # 2. Điền biến
    full_prompt = system_prompt.format(
        original_intent=state['input_prompt'],
        react_code=state.get("react_code", "")
    )
    
    response = llm.invoke(full_prompt)
    
    return {"playwright_test_code": response.content}