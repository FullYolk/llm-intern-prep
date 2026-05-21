## 修day10bug
* tools路由需要防御不存在的工具名
* json.loads需要异常保护
* get_weather Python引用陷阱
* eval实际工程危险
* messages最终应该是符合API协议的结构化dict/list
## schemas定义pydantic模型
* session_id:区分对话
* message/reply:实际信息
* 实际工程中 Request需要：stream:bool(是否流式输出) model:str(允许用户切换模型) user_id(token扣减或权限校验)
* Response需要: usage字段和created_at(时间戳)
## llm_service
* response.choice[0].message.content才是纯字符串
* 核心路由要捕捉异常
* controller层要和service层分离
## 注意事项
* 前端不直接调API：安全 业务控制（无法注入system prompt 无法连接数据库等）
* 后端保护APIKEY：代理模式+环境变量
* 字典存历史：内存爆炸OOM 多进程不共享记忆
* 使用Redis可以设置TTL 同时所有进程都有统一的Redis解决
* 请求体:Request Body
* 响应体：Response Model
## 算法
* 字符串解码：用栈处理嵌套
* 最大股票利润：考虑贪心算法记录全局最小值与最大利润 复习滑动窗口最大值（单调队列）