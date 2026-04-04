# frontend/services/api_service.py
import requests
from config.settings import settings

def generate_react_code(prompt: str, visual_context: dict):
    """
    Gọi API POST /api/generate của Backend
    """
    url = f"{settings.BACKEND_URL}/api/generate"
    
    payload = {
        "prompt": prompt,
        "visual_context": visual_context
    }
    
    try:
        print(f"🔄 Đang gọi API: {url}")
        response = requests.post(url, json=payload)
        response.raise_for_status() # Raise error nếu status code != 200
        
        return response.json()
        
    except requests.exceptions.RequestException as e:
        return {"status": "error", "error_message": str(e)}