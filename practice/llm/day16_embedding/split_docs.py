from langchain_text_splitters import RecursiveCharacterTextSplitter
from load_docs import load_markdown_docs

def split_documents():
    docs = load_markdown_docs("data")
    splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
    )
    chunks = splitter.split_documents(docs)
    return chunks