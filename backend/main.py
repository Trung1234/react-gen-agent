# backend/main.py
from fastapi import FastAPI, HTTPException
from models.schemas import GenerateRequest, GenerateResponse
from graph.workflow import create_graph

app = FastAPI(title="AI React Generator API")

# Khởi tạo Graph một lần khi start app
graph_app = create_graph()

@app.get("/")
def home():
    return {"message": "AI React Generator Backend is running!"}

@app.post("/api/generate", response_model=GenerateResponse)
async def generate_code(request: GenerateRequest):
    try:
        print(f"Nhận request: {request.prompt}")
        
        # 1. Chuẩn bị dữ liệu đầu vào cho Graph
        initial_state = {
            "input_prompt": request.prompt,
            "visual_context": request.visual_context,
            "messages": [],
            "react_code": None,
            "syntax_error": None,
            "is_valid": False
        }

        # 2. Chạy LangGraph
        # config={"recursion_limit": 5} để tránh lặp vô hạn nếu lỗi không sửa được
        final_state = graph_app.invoke(initial_state, config={"recursion_limit": 5})

        # 3. Trả kết quả
        return GenerateResponse(
             status="success",
            react_code=final_state.get("react_code"),             # Phải giống tên field ở schemas
            playwright_test_code=final_state.get("playwright_test_code"), # Phải giống tên field ở schemas
            logs=final_state.get("messages")
        )

    except Exception as e:
        print(f"Lỗi hệ thống: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)