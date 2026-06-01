# Tech Notes RAG QA

## 项目简介
一个基于 FastAPI + Chroma + OpenAI-compatible LLM 的技术笔记 RAG 问答服务。
支持对 Markdown 技术文档进行向量化检索，并基于检索上下文生成答案，同时返回来源信息。

## 技术栈
- Python
- FastAPI
- LangChain
- Chroma
- OpenAI-compatible API
- Pydantic

## 核心功能
- Markdown 文档加载
- 文本切分
- Embedding 向量化
- 向量检索 top-k
- 基于上下文回答问题
- 返回引用来源
- FastAPI /ask 接口

## 项目结构
day18_rag_api/
├── main.py                # FastAPI 路由入口
├── rag_service.py         # 核心业务层（原生 RAG 实现）
├── schemas.py             # 数据契约层（Pydantic 校验模型）
├── embedding.py           # 向量化模型单例封装
├── rag_langchain_demo.py  # LangChain / LCEL 对照实现版本
├── chroma_db/             # 本地向量库持久化目录
└── .env                   # 环境变量配置

## 快速开始
* 在根目录创建.env文件并添加以下变量：
```
LLM_API_KEY="your_api_key"
LLM_BASE_URL="your_base_url"
LLM_MODEL="your_model_name"
EMBEDDING_API_KEY="..."
EMBEDDING_BASE_URL="..."
EMBEDDING_MODEL="..."
```
* 启动服务
```
uvicorn main:app --reload
```

* API调试
通过浏览器自动生成的swagger文档进行调试

## 示例问题
- 什么是RAG？
- 什么时候应该使用RAG？
- RAG的全链路是什么？
- 什么是Tool Calling？

## 已知问题
- 当前数据集较小
- 检索结果可能集中于同一文档
- 尚未实现 rerank / hybrid search / query rewrite

## 优化计划
* 当前每次请求都重新加载Chroma 需重构为全局单例或注入liffespan
* 目前仅依赖基础的余弦相似度检索 计划引入query rewrite和rerank
* 后续添加流式支持
* 使用Docker构建镜像 一键部署