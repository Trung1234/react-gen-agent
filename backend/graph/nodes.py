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
    
    system_prompt = load_prompt("code_agent.md")
    
    full_prompt = system_prompt.format(
        tech_analysis=tech_analysis,
        visual_context=state['visual_context'],
        error_log=state.get("error_log", "None")
    )
    
    response = llm.invoke(full_prompt)
    
    return {
        "react_code": response.content, 
        "error_log": None
    }

def test_agent(state: AgentState):
    """Agent 3: Viết Playwright Test Case (Đã sửa tên để khớp workflow.py)"""
    print("🧪 [Test Agent] Đang tạo Playwright Test...")
    
    system_prompt = load_prompt("test_agent.md")
    
    full_prompt = system_prompt.format(
        original_intent=state['input_prompt'],
        react_code=state.get("react_code", "")
    )
    
    response = llm.invoke(full_prompt)
    
    return {"playwright_test_code": response.content}