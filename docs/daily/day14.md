## 修day13BUG
* 模型输出风格 稳定性 随机性都应该显式配置 而不是依赖默认值
* PydanticOutputParser负责给模型格式说明 并把输出解析成Pydantic对象。如果输出不符合格式，会抛异常，自动修复需要OutputFixingParser,RetryOutputParser或自行编写Retry逻辑。
## LangChain进阶
* JsonOutputParser: 封装好了JSON提取的功能 避免重复造轮子 但最重要的优势如下：Markdown格式清洗（最实用） 统一工作流（直接用管道符连接成chain 保持代码的整洁） 并且支持了流式JSON
* 但它的缺点是只能保证输出是字典 并不能保证有哪些Key
* PydanticOutputParser: 需要将具体的Pydantic类作为参数进行传递
* 保证了获得结果的格式 同时能够保证类型校验 安全性得到保障
* 但缺点是会遇到大模型的幻觉问题 此时需要：
* 作为结构化抽取任务 先将temperature降低为0消除随机性，同时在System Prompt中明确字段约束，同时可以提供Few-shot，通过In-Context Learning来强制模型对齐格式。
* 在复杂的生产环境中，可以引入 LangChain 的 PydanticOutputParser。将数据结构定义为Pydantic Model，并在关键字段上使用Optional与Field(description=) 这样当出现格式问题时 可以第一时间捕获异常。
* 当异常产生之后，利用重试机制将错误JSON和报错信息重新返回给LLM。当重试超过最大次数时，再触发降级逻辑或人工修复。
* batch:将列表中的每一个字典，并发跑一遍invoke()，所以要求每一个字典都有prompt模板要求的所有变量
* 真实生产中，我们可以使用提示词模板的partial（偏函数绑定）功能，提前注入静态变量，例如：
* ### 概念代码，看懂思路即可
prompt = ChatPromptTemplate.from_messages([...])

### 提前把 format_instructions 填进去，生成一个“半成品”Prompt
partial_prompt = prompt.partial(format_instructions=parser.get_format_instructions())

### 现在的链条里，Prompt 只缺 text 这一块拼图了
chain = partial_prompt | llm | parser

### 完美！batch 只需要传 text 即可
chain.batch([{"text": "张三..."}, {"text": "李四..."}])
* 流式输出部分：LangChain的hain.stream() 确实把大模型的残缺 Chunk 拼成了干净的纯文本，但并没有封装成SSE格式。在FastAPI里集成时，我们必须自己做一次包装，将纯文本打包成SSE协议，并推送给前端。
* 对于batch，为了防止被误判为DDoS攻击，生产中必须配置config={"max_concurrency":xxx}来限制并发数
* 在后端框架中 不要使用chain.stream(),必须使用异步版本:chain.astream()
* RunnableParallel(分流器): 将prompt分成多个变量，例如在RAG项目中:setup_and_retrieval = RunnableParallel(
    # 支流 1：把用户问题拿去查数据库，返回一堆文档给 context
    context=retriever, 
    # 支流 2：保留用户问题原样，给 question
    question=RunnablePassthrough() 
)

* RunnablePassthrough(直流管):
* 由于LCEL要求所有使用|或在RunnableParallel中的内容，必须是一个Runnable,所以不需要使用大量中间变量处理并发检索和参数组装，直接使用字典结构就可以处理好数据的流向。
* LCEL语法的精髓就是将命令式编程变成了声明式编程。

## LangGraph入门
* LangGraph实际上是把复杂的分支条件 显式的建模成图结构状态机 因此更加适合具有循环、分支、工具调用的复杂 Agent 工作流。
* 在早期的 LangGraph 中，强制要求状态是一个字典。最新版已经支持BaseModel做状态 但TypedDicr依然是标准写法
* 节点函数并不需要返回完整的字典 LangGraph会自动合并覆盖到全局状态中 完成局部更新。
* 图中的每个节点都是一个普通的Python函数，它会接受当前的state，并必须返回一个字典，里面只包含想要更新的字段
* 路由函数同样接受整个state 必须返回一个字符串 这个字符串必须是路由字典中的key
* 程序启动时：连接START
* 结束时：连接END
* 在工作流进行时 每个节点只负责修改状态字典中的category 随后由路由函数进行负责 它根据这个字段动态决定继续将任务交给哪个节点 这就是LangGraph的数据驱动流转 业务逻辑清晰 而且局部更新能够做到数据的无缝缝合

## 算法
* 二叉树中序遍历 内部定义辅助函数方便返回(Python技巧)
* 最大深度 自下而上的计数
* 翻转二叉树 自下而上的反转
* 层序遍历 利用双端队列的BFS 处理每一层时：先出队 再让孩子入队 注意算好循环次数（等于每一层的大小）