from embedding import get_embeddings
from openai import OpenAI
import os
from dotenv import load_dotenv
from pathlib import Path
from langchain_chroma import Chroma

load_dotenv()

LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_BASE_URL = os.getenv("LLM_BASE_URL")
LLM_MODEL = os.getenv("LLM_MODEL")

client = OpenAI(
    api_key=LLM_API_KEY,
    base_url=LLM_BASE_URL
)

current_dir = Path(__file__).parent
PERSIST_DIR = str(current_dir/"chroma_db")

def build_context(results:list) -> str:
    res = ""
    for (doc, score) in results:
        res = res + "[来源:" + doc.metadata.get('filename') + "]" + doc.page_content + "\n"
    return res

def answer_with_rag(query:str, k:int =3):
    vector_store = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=get_embeddings()
    )
    results = vector_store.similarity_search_with_score(query=query,k=k)
    context = build_context(results)
    system_prompt="你是一个严谨的助手。请你【只根据】下面的参考资料回答问题。如果资料里没有，你就回答“不知道”，严禁胡编乱造！"
    user_prompt=f"问题:{query} 参考资料:{context}"
    messages = [{"role":"system","content":system_prompt},{"role":"user","content":user_prompt}]
    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=messages,
        temperature=0.0
    )
    sources = []
    for (doc, score) in results:
        sources.append(doc.metadata.get("filename"))
    return {"answer":response.choices[0].message.content,"sources":sources}

def main():
    while 1:
        s = input("请输入向大模型提问的问题")
        if s == "exit":
            break
        print(answer_with_rag(s))
        
if __name__ == "__main__":
    main()