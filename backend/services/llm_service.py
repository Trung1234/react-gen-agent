# backend/services/llm_service.py
from langchain_google_genai import ChatGoogleGenerativeAI
from config import settings

def get_llm():
    """
    Khởi tạo và trả về instance của LLM Gemini.
    """
    return ChatGoogleGenerativeAI(
        model=settings.MODEL_NAME,
        temperature=settings.TEMPERATURE,
        api_key=settings.GOOGLE_API_KEY
    )