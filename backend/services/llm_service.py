# backend/services/llm_service.py
# Import chuyên dụng cho Azure thay vì ChatOpenAI
from langchain_openai import AzureChatOpenAI 
from config import settings

def get_llm():
    """
    Khởi tạo LLM kết nối tới Azure OpenAI dùng class chuyên biệt.
    """
    return AzureChatOpenAI(
        openai_api_key=settings.AZURE_OPENAI_API_KEY,
        azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
        api_version=settings.AZURE_OPENAI_API_VERSION,
        deployment_name=settings.AZURE_DEPLOYMENT_NAME,
        temperature=0
    )