import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()
def get_embeddings() -> OpenAIEmbeddings:
    API_KEY = os.getenv("EMBEDDING_API_KEY")
    BASE_URL = os.getenv("EMBEDDING_BASE_URL")
    MODEL = os.getenv("EMBEDDING_MODEL")

    if not API_KEY or not BASE_URL or not MODEL:
        raise ValueError("错误:Embedding配置缺失 请检查.env")

    embeddings = OpenAIEmbeddings(
        api_key=API_KEY,
        base_url=BASE_URL,
        model=MODEL
    )

    return embeddings

def main():
    print("测试embedding接口...")

    emb_model=get_embeddings()
    text_to_embed = "Agent为什么需要Tool Calling?"

    vector = emb_model.embed_query(text_to_embed)

    print(f" 向量维度大小: {len(vector)}")
    print(f" 向量前 5 个数字预览: {vector[:5]}")

if __name__ == "__main__":
    main()