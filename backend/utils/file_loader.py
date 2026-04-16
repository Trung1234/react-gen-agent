# backend/utils/file_loader.py
import os

# Đường dẫn tuyệt đối đến thư mục prompts
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")

def load_prompt(file_name: str) -> str:
    """
    Đọc nội dung file .md từ thư mục prompts
    """
    file_path = os.path.join(PROMPTS_DIR, file_name)
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"❌ Không tìm thấy file prompt: {file_path}")
        return "" # Fallback rỗng