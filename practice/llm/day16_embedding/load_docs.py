from langchain_core.documents import Document
from pathlib import Path

def load_markdown_docs(data_dir: str) -> list[Document]:
    docs = []
    current_dir = Path(__file__).parent
    real_data_path = current_dir/data_dir

    for path in real_data_path.glob("*.md"):
        text = path.read_text(encoding="utf-8")
        docs.append(Document(
            page_content=text,
            metadata={
                "source": str(path),
                "filename":path.name,
                "file_type":path.suffix,
                }
        ))
    return docs



def main():
    docs=load_markdown_docs("data")
    print(f"loaded docs:{len(docs)}")
    for doc in docs:
        print(doc.metadata)
        print(doc.page_content[:100])

if __name__ == "__main__":
    main()