# backend/graph/nodes.py
from .state import AgentState
from services.llm_service import get_llm
from utils.file_loader import load_prompt

llm = get_llm()

def intent_node(state: AgentState):
    """Agent 1: Phân tích ý định"""
    print("🤖 [Intent Node] Đang phân tích yêu cầu...")
    
    system_prompt = load_prompt("intent_agent.md")
    
    full_prompt = system_prompt.format(
        user_request=state['input_prompt'],
        visual_context=state['visual_context']
    )
    
    response = llm.invoke(full_prompt)
    return {"messages": [f"Intent Analysis: {response.content}"]}

def code_node(state: AgentState):
    """Agent 2: Viết code React"""
    print("👨‍💻 [Code Agent] Đang sinh code React...")
    
    tech_analysis = state['messages'][-1] if state['messages'] else state['input_prompt']
    
    # 1. Load prompt
    system_prompt = load_prompt("code_agent.md")
    
    # --- DEBUG: In ra prompt xem có rỗng không ---
    if not system_prompt:
        print("⚠️ CẢNH BÁO: System prompt bị RỖNG! Hãy kiểm tra file code_agent.md")
    else:
        print(f"📄 Prompt length: {len(system_prompt)} chars")
    
    full_prompt = system_prompt.format(
        tech_analysis=tech_analysis,
        visual_context=state['visual_context'],
        error_log=state.get("error_log", "None")
    )
    
    response = llm.invoke(full_prompt)
    
    # --- DEBUG: In ra kết quả thô từ Azure ---
    print(f"🔍 Raw Response Type: {type(response)}")
    print(f"🔍 Raw Response Content (100 chars đầu): {response.content[:100]}")
    
    code_result = response.content.strip() if response.content else ""
    
    return {
        "react_code": code_result, 
        "error_log": None
    }

def test_agent(state: AgentState):
    """Agent 3: Viết Playwright Test Case"""
    print("🧪 [Test Agent] Đang tạo Playwright Test...")
    
    system_prompt = load_prompt("test_agent.md")
    
    # --- DEBUG ---
    if not system_prompt:
        print("⚠️ CẢNH BÁO: System prompt bị RỖNG! Hãy kiểm tra file test_agent.md")

    full_prompt = system_prompt.format(
        original_intent=state['input_prompt'],
        react_code=state.get("react_code", "")
    )
    
    response = llm.invoke(full_prompt)
    
    # --- DEBUG ---
    print(f"🔍 Raw Test Content (100 chars đầu): {response.content[:100]}")
    
    test_result = response.content.strip() if response.content else ""
    
    return {"playwright_test_code": test_result}