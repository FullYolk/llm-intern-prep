from langchain_core.runnables import RunnablePassthrough, RunnableParallel

chain = RunnablePassthrough()

print(chain.invoke("任何内容"))

parallel_chain = RunnableParallel(
    origin=RunnablePassthrough(),
    upper=lambda x: x.upper(),
    length=lambda x: len(x)
)

result = parallel_chain.invoke("hello")
print(result)