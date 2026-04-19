## Project Mermaid

<img width="2048" height="1117" alt="image" src="https://github.com/user-attachments/assets/d7f14e0a-38d7-4b85-849c-2bfd1c80c5be" />

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
frontend/
├── .env                    # Chứa biến môi trường (URL Backend, API Keys)
├── .gitignore
├── README.md
├── requirements.txt        # Các thư viện cần thiết
├── app.py                  # File chính chạy ứng dụng (Entry point)
│
├── config/                 # Cấu hình dự án
│   ├── __init__.py
│   └── settings.py         # Đường dẫn API, constants
│
├── services/               # Xử lý logic gọi Backend (Requests)
│   ├── __init__.py
│   └── api_service.py      # Các hàm gọi API Orchestrator, Test, etc.
│
├── ui/                     # Các component giao diện (tách file để gọn gàng)
│   ├── __init__.py
│   ├── design_section.py   # Màn hình nhập Design/Original Input
│   ├── code_section.py     # Hiển thị code sinh ra bởi Code Agent
│   └── test_section.py     # Hiển thị kết quả Selenium & Visual Regression
│
└── utils/                  # Hàm tiện ích
    ├── __init__.py
    ├── helpers.py          # Các hàm xử lý hình ảnh, text chung
    └── styles.css          # Tùy chỉnh CSS cho Streamlit (nếu cần)

```
 ##  COnfig  on Environment variables
```text
[
  {
    "name": "AZURE_DEPLOYMENT_NAME",
    "value": "gpt-5.4-mini",
    "slotSetting": false
  },
  {
    "name": "AZURE_OPENAI_API_KEY",
    "value": "",
    "slotSetting": false
  },
  {
    "name": "AZURE_OPENAI_API_VERSION",
    "value": "2024-12-01-preview",
    "slotSetting": false
  },
  {
    "name": "AZURE_OPENAI_ENDPOINT",
    "value": "ht/",
    "slotSetting": false
  },
  {
    "name": "BACKEND_URL",
    "value": "https://get",
    "slotSetting": false
  },
  {
    "name": "SCM_DO_BUILD_DURING_DEPLOYMENT",
    "value": "true",
    "slotSetting": false
  },
  {
    "name": "WEBSITE_RUN_FROM_PACKAGE",
    "value": "0",
    "slotSetting": false
  }
]

```
