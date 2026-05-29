import inspect
from pathlib import Path
from langchain_chroma import Chroma
from split_docs import split_documents
from embedding import get_embeddings
current_dir = Path(__file__).parent

PERSIST_DIR = str(current_dir / "chroma_db")

def build_vectorstore():
    print("加载和切分文档...")
    chunks = split_documents()
    print(f"已切分出{len(chunks)}个chunks")

    print("加载embedding模型...")
    embeddings = get_embeddings()

    print("建库...")
    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=PERSIST_DIR
    )

    print("建库完成")
    return vectorstore

if __name__ == "__main__":
    build_vectorstore()