backend/
├── .env                  # Lưu API Keys
├── main.py               # Entry point: Khởi chạy FastAPI Server
├── requirements.txt      # Danh sách thư viện
├── config.py             # Cấu hình hệ thống (tên model, giới hạn...)
├── models/
│   └── schemas.py        # Pydantic models cho Request/Response API
├── services/
│   └── llm_service.py    # Khởi tạo đối tượng LLM (Gemini)
└── graph/
    ├── __init__.py
    ├── state.py          # Định nghĩa State (TypedDict) cho LangGraph
    ├── nodes.py          # Chứa logic các Agent (Intent, Code, Validator)
    └── workflow.py       # Nối các Node lại thành Đồ thị (Graph)