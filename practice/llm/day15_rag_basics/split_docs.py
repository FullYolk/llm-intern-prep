from langchain_text_splitters import RecursiveCharacterTextSplitter
from load_docs import load_markdown_docs

docs = load_markdown_docs("data")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50,
)
chunks = splitter.split_documents(docs)
print(f"原始文档数:{len(docs)}")
print(f"切分后chunk数:{len(chunks)}")

for i, chunk in enumerate(chunks[:5]):
    print("-"*20)
    print(f"chunk{i}")
    print(chunk.metadata)
    print(chunk.page_content)