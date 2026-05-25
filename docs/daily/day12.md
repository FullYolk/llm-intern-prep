## 修day11 bug
* 加Logging
* exc_info=True 自动打出错误调用栈 方便定位BUG
* 对话历史截断：先切掉system 再取后N条 然后拼接 即history[1:][-MAX_HISTORY_MESSAGE:] 
## SSE流式输出添加
* 优点：首字响应延迟低
* 开启stream = True参数
* 遍历数据流（返回的数据类型不同）
* 返回结构在chunk.choices[0].delta.content
* yield出去
## 日志与异常捕获
* 记录请求：做输入脱敏（只取前十个字或记录长度）
* 报错后要用SSE格式发给前端
* 因为流式传输时 HTTP连接已经建立成功 不能改变状态码
* 只能通过发送一段特殊的文本流来通知前端