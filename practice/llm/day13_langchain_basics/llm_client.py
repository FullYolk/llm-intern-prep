from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
API_KEY = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("LLM_BASE_URL")
MODEL_NAME = os.getenv("LLM_MODEL")

def get_client():
    if not API_KEY:
        raise ValueError("LLM_API_KEY未配置")
    if not BASE_URL:
        raise ValueError("LLM_BASE_URL未配置")
    if not MODEL_NAME:
        raise ValueError("LLM_MODEL未配置")
    client = OpenAI(api_key=API_KEY,base_url=BASE_URL,model=MODEL_NAME)
    return client