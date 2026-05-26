from langchain_text_splitters import RecursiveCharacterTextSplitter
from load_docs import load_markdown_docs

def main():
    docs = load_markdown_docs("data")
    print(f"原始文档总数:{len(docs)}")
    print("-"*20)

    test_sizes = [50,100,300,500]

    fixed_overlap = 20

    for size in test_sizes:
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=size,
            chunk_overlap=fixed_overlap,
        )
        chunks = splitter.split_documents(docs)
        print(f"参数调优: chunk_size = {size}")
        print(f"实验结果: 共切分出 {len(chunks)} 个 chunk")
        
        
        print(f"样本预览: {chunks[0].page_content[:30]}...")
        print("-" * 20)
if __name__ == "__main__":
    main()
