from langchain_chroma import Chroma
from embedding import get_embeddings
from pathlib import Path

current_dir = Path(__file__).parent
PERSIST_DIR = str(current_dir/"chroma_db")

def search(query:str, k:int =3 ):
    vectorstore = Chroma(
        persist_directory=PERSIST_DIR,
        embedding_function=get_embeddings()
    )

    results = vectorstore.similarity_search_with_score(query,k=k)

    print("-" * 50)

    for i, (doc, score) in enumerate(results, 1):
        # score 通常是距离，越小表示越相似（具体取决于距离算法，如果是 Cosine 通常也是越小距离越近）
        print(f" Rank {i} | 距离得分: {score:.4f}")
        print(f" 来源: {doc.metadata.get('filename')}")
        print(f" 内容: {doc.page_content.strip()}")
        print("-" * 50)

if __name__ == "__main__":
    search("RAG全过程是什么？")