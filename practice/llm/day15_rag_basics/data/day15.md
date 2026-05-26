## RAG文件加载
* 常规场景可以直接读入内存
* 海量工业场景不能使用 必须使用lazy loading/生成器：
def lazy_load_docs(data_dir):
    for path in Path(data_dir).glob("*.md"):
        text = path.read_text()
        # 不是放进 list 里，而是读一个交出去一个
        yield Document(page_content=text, metadata={"source": str(path)})