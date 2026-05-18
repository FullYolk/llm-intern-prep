from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()
API_KEY = os.getenv("LLM_API_KEY")
BASE_URL = os.getenv("LLM_BASE_URL")
MODEL_NAME = os.getenv("LLM_MODEL")

def get_client():
    client = OpenAI(api_key=API_KEY,base_url=BASE_URL)
    return client