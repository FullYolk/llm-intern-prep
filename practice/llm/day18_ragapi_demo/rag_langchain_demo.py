from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from embedding import get_embeddings
from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_BASE_URL = os.getenv("LLM_BASE_URL")
LLM_MODEL = os.getenv("LLM_MODEL")

if not LLM_API_KEY or not LLM_BASE_URL or not LLM_MODEL:
    raise ValueError("错误：LLM API 配置缺失 请检查.env")

current_dir = Path(__file__).parent
PERSIST_DIR = str(current_dir/"chroma_db")
vector_store = Chroma(
    persist_directory=PERSIST_DIR,
    embedding_function=get_embeddings()
)

retriever = vector_store.as_retriever(search_kwargs={"k":3})

prompt = ChatPromptTemplate.from_messages([
    ("system","你是一个严谨的助手，请【只根据】以下参考资料回答问题。如果没找到答案，就回答“不知道”。\n\n参考资料：\n{context}"),
    ("user","问题:{question}")
])

llm = ChatOpenAI(
    api_key=LLM_API_KEY,
    base_url=LLM_BASE_URL,
    model=LLM_MODEL,
    temperature=0.0
)

def format_docs(docs):
    return "\n\n".join([doc.page_content for doc in docs])

rag_chain = (
    {
        "context":retriever|format_docs,
        "question":RunnablePassthrough()
    }
    |prompt
    |llm
    |StrOutputParser()
)

def main():
    question = "什么是RAG？"
    print(f"问题{question}")
    answer = rag_chain.invoke(question)
    print(f"回答：{answer}")

if __name__ == "__main__":
    main()