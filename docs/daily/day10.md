## 修day9bug
* 在加载json前要做空值保护
* 具体异常打印更利于debug
* 善用model_json_schema自动化强化prompt
* 不要用python关键字做变量名！
## Tool Calling
* 概念:Tool Calling本质上是一种结构化意图识别和参数提取机制。大模型本身不会执行任何代码，它通过阅读我们提供的工具说明，判断是否需要调用工具，并生成合法的JSON格式的调用请求；而后端代码才是真正的执行者，负责拦截这个请求，真实运行Python函数，并把结果返回给大模型。
* 具体的tool Call格式：是一个列表（里面是字典） 参数为id (工具调用的标识符 用于上下文匹配) type:function function:{"name":"xxx" "arguments":"字符串化的JSON"} arguments是一个带转义符的字符串 而不是字典 因此必须显式调用一次json.loads反序列化为字典 再进行操作
## Schema
* 概念：Schema是大模型与外部系统进行通信的API契约。由于大模型无法直接读取后端的源码，我们必须用JSON格式（JSON schema规范）将函数的名称，描述以及各个参数的类型和要求精确的向大模型描述。实际上也是prompt的一部分，但它直接决定了模型是否能正确触发工具调用和参数生成。
* Schema包含三部分：name 函数名 description 函数描述 parameters 参数规范
* 后端python函数收到参数后 仍然需要做校验，有可能出现参数数量 类型或工具错误 必须使用pydantic或手写逻辑二次校验 失败的话就将报错信息重新返回给大模型重试。
## 做一个tool calling链路
* 准备Mock tool(统一接口 实际工程中接对应API)
* 编写schema:重点是格式与description 函数以及每个参数都要有具体的描述
* 完整主流程：构造messages -> 调用模型 传入tools=tools ->判断模型是否返回tool_calls -> 后端通过路由执行函数 ->将工具结果追加回messages ->再调用一次模型 做最终回答
## 实际tool calling中需要注意的
* 连续思考与多步工具调用
* 并行工具调用(asyncio 协程 并发执行)
* 容错：生成假函数名或不合法字符串：处理异常 将异常结果重新返回给大模型
* 对于大量的数据 要做上下文截断/摘要提取
## 算法
* 每日温度：单调栈
* 区间合并：排序+贪心