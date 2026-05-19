## 修day8bug
* 做一些空响应保护 配置校验
* 特殊情况一定考虑到
## 四个prompt基础实验
* system prompt的约束：
* system prompt为模型设定了极强的先验条件 极大约束了输出边界和风格
* few-shot上下文学习：
* 模型会自动模仿虚拟上下文的例子 甚至能够限制模型按照特定的格式进行输出 应用在：复杂意图分类/路由 内部黑化/专有名词提取 应对边缘情况/异常处理 动态few-shot（用RAG搜索 动态拼接到messages里）
* temperature:反映的选择出现概率最高词汇的程度 越低越保守稳定 越高越有创造力（选择更冒险的词汇 较为发散）
* temp=0依然不完全稳定 原因是浮点数计算误差 MoE架构的路由策略与官方的底层随机性 但对于JSON输出和代码生成 即使不完美 我们还是要将温度设为0.0保证稳定性
* 输出格式限制：prompt对大模型进行输出进行严格约束
* 在实际生产中 优化大模型输出稳定性：首先通过 System Prompt 明确角色和约束；如果格式依然不稳定，我会引入 2-3 个 Few-shot 示例，利用 In-Context Learning 让模型模仿；在参数层面，如果是做结构化抽取，我会坚决把 Temperature 降到 0 消除随机性。如果这些都不行，才会考虑微调（Fine-tuning）。
## 结构化输出demo
* 让模型输出prompt字符串 主要方式：
* system prompt限制（可以借助schema注入的方式 调用StudentProfile.model_json_schema()将类转化为JSON结构描述 动态拼接到prompt里） 降低模型温度（0） 用few-shot预学习 同时尝试开启API的JSON MODE强制输出结构（response_format={ "type": "json_object" }）
* 取得输出之后 在代码层用正则表达式清洗（去除markdown标记） 如果仍然失败 则将错误栈作为上下文返回给大模型 让它进行自我纠错
## JD筛选AGENTdemo：
* 同时应用pydantic模型与上下文工程等知识
* 后续可以接入数据库 方便查找
* 实际应用中的输入流：通过HTTP请求获得前端JSON 解析文件 爬虫与数据库拉取 消息队列（redis等）
## 算法：
* 滑动窗口最大值：双端单调队列 注意条件
* 最大子数组和 DP+贪心