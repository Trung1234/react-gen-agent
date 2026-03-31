## Cấu trúc thư mục (Project Structure)

```text
backend/
├── .env                  # Lưu API Keys (không commit lên Git)
├── main.py               # Entry point: Khởi chạy FastAPI Server
├── requirements.txt      # Danh sách thư viện cần thiết
├── config.py             # Cấu hình hệ thống (tên model, giới hạn, settings)
├── models/
│   └── schemas.py        # Pydantic models cho Request/Response API
├── services/
│   └── llm_service.py    # Khởi tạo đối tượng LLM (Gemini)
└── graph/
    ├── __init__.py       # Khởi tạo package graph
    ├── state.py          # Định nghĩa State (TypedDict) cho LangGraph
    ├── nodes.py          # Chứa logic các Agent (Intent, Code, Validator)
    └── workflow.py       # Nối các Node lại thành Đồ thị (Graph)
