## 修day7bug
* 注意语法
* 中间件用logging
## API调用demo
* 使用OpenAI-compatible API：第三方模型供应商（如 DeepSeek、智谱 AI、硅基流动等）在提供服务时，完全遵循了 OpenAI 定义的 HTTP 接口规范、请求体结构和响应格式。能够降低迁移成本 （无需学习新SDK 只需修改base_url与api_key即可切换模型） 保证生态协同：现有llm工具链大多优先支持OPENAI协议 且已经成为行业实施标准
* 永远不要在函数内写死APIKEY！（保证安全）
* message的不同类型：system:全局设定。用于定义机器人的‘人设’、遵守的规则和预置的知识背景。user：用户。代表人类的指令或提问。assistant：模型。代表 AI 之前的回复。tool / function：工具回调。当模型请求调用外部工具后，由后端将执行结果返回给模型
* 多轮对话：用list存历史再拼接
## 异常处理
* 捕获一些常见的OpenAI SDK异常：openai.RateLimitError：请求太频繁或欠费了。处理策略：等待一会儿再试。
openai.APIConnectionError：网络不通（比如你的代理挂了）。处理策略：检查网络。
openai.AuthenticationError：API Key 错了或失效了。
openai.APITimeoutError：请求时间过长
* 设置timeout参数
* 空值保护：检查response.choices与content
* 做logging规范化：info warning error critical做不同管理
* logging落盘：可以做日志切分（按大小或时间）/结构化日志
* RotatingFileHandler：当文件达到一定大小时 重命名给旧文件 使用新文件
* 指数退避重试 (Exponential Backoff)：等待合适的时间再充实
* 优雅降级策略（超时）：重试（换便宜快速的模型） 查看是否命中缓存 友好回执（返回预设的系统繁忙提示）
* 敏感信息脱敏：在记录 Messages 到日志前，使用正则表达式或简单的字符串替换，把敏感信息处理掉。
## 其他
* temperature（采样温度）是一个控制模型输出确定性（Determinism）和随机性（Randomness）的超参数。其取值范围通常在 0 到 2 之间。物理意义（底层原理）：
在模型输出层，它会计算每个 token 的概率分布。temperature 作用于 Softmax 函数之前：

低 Temperature (< 0.5)：会让高概率的 token 概率更高，低概率的更低。模型表现得更‘保守’、‘理智’，适合生成代码、数学、逻辑推理。
高 Temperature (> 1.0)：会让概率分布变得‘平滑’，增加低概率 token 被选中的机会。模型表现得更‘有创意’、‘发散’，适合文学创作、头脑风暴。
最佳实践：
在 Agent 开发中，如果需要模型严格遵循 JSON 格式或执行工具，通常建议将 temperature 设为 0 或非常接近 0 的值，以保证输出的稳定性。”
* “在实际生产环境中，除了余额和网络，我们经常遇到以下几类错误，这些都需要在代码中进行特定的异常处理：

Context Window Exceeded（上下文超限）：
发送的 messages 列表总 Token 数超过了模型支持的最大限度（如 128k）。这是 Agent 开发中最常见的错误，需要通过‘滑动窗口’或‘总结历史’来解决。

Rate Limit Reached (429 Error)：
虽然有余额，但单位时间内的请求频率（RPM）或消耗的 Token 数（TPM）超过了账户分级限制。

Content Moderation（内容审核拦截）：
输入内容或模型试图生成的输出内容触发了供应商的安全过滤机制（如涉黄、涉政、暴力），导致请求被强制中断。

Invalid Schema（结构化错误）：
在开启 JSON Mode 或 Tool Calling 时，模型生成的回复不符合预定义的 JSON Schema，导致解析失败。

Model Deprecated / Maintenance（模型维护）：
调用的模型版本已被废弃（404）或服务端当前正处于高负载拥堵状态（503）。

Parameter Out of Range：
传入了模型不支持的参数。例如，某些模型不支持超过 1.0 的 temperature，或者 max_tokens 设得太大。”

## 算法
* 频率最大的topk元素
* 使用Counter:自动计数各个数字出现的次数
* 返回格式是List[{num:freq}]
* 堆：使用python实现的heapq
* heapq.heappush与heapq.heappop（默认为小顶堆）# 大顶堆怎么操作？
* 取元组：可以用列表推导式（类似数组的方式） 也可以用元组解包
* 数组中最大的第K元素：同样用小顶堆