from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "你是一个资深的程序员，你总是用{style}的语气回答问题。"),
    ("human", "请帮我解释一下什么是 {topic}？")
])

formatted_prompt = prompt_template.invoke({
    "style": "极度暴躁但又很靠谱",
    "topic": "FastAPI"
})

print("1. 打印原始对象：")
print(formatted_prompt)
print("\n" + "="*50 + "\n")
print("2. 打印底层真实的 message 列表（重点看这个）：")
print(formatted_prompt.to_messages())