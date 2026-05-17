## 修day5bug：
* 装饰器参数里加response_model:数据脱敏与过滤（fastapi自动修正数据类型 剔除无关数据后再发给前端） 出口数据校验 补全swagger文档
* status_code（HTTP状态码）:200:OK 201：Created(成功受到请求并创建实体资源)
## 异常处理进阶
* Exception:Python原生异常基类 纯业务代码遇到错误跑出异常
* HTTPException:预期中的业务逻辑拒绝 是我们主动预判到不合理操作时抛出的异常 本身就是FastAPI提供的类 自带HTTP状态码 写在顶层的路由函数中
* 自定义异常：业务中自定义的异常 可以在web层拦截
* 全局异常处理器：全局拦截异常 处理非预期的系统崩溃 将所有未知的500错误拦截 转化为更友好的报错 自定义处理方式 可以配合自定义异常进行使用处理 将错误翻译成HTTP状态码返回给前端
* 在真实项目中 如果让500异常直接冒到前端 会返回堆栈错误代码 不利于项目的安全性 同时由于返回的不是标准JSON 前端无法处理解析
* 统一异常管理格式 有利于前端解析 安全啊防止泄露 方便定位BUG 还能够有利于多语言 多标准支持
## 中间件
* 中间件位于前端请求和路由函数中间
* 格式：@app.middleware("http") async def log_middleware(request: Request, call_next): response = await call_next(request)
* 相比于普通装饰器 中间件的优势是只写一次 全局生效
* 非常适合做日志 记录 限流 追踪等
* 实际应用：IP黑名单拦截 全局扣费 追踪链路ID等
* 做日志的必要性：方便监控程序运行 定位BUG等
## 文件传输
* 格式：def upload_file(file:UploadFile = File(...)) 我们有 file.filename file.size
* 由于涉及io 我们用 async def与await
* 实际情况下 为了防止OOM 我们使用shutil.copyfileobj(file.file,文件指针)拷贝到本地
* 如果使用bytes处理大文件 会导致OOM 文件会全部传入服务器内存中
* 而UploadFile有SpooledTemporaryFile机制 一旦文件超过1MB 会直接写入硬盘 内存占用极小
* 检查后缀时 可以检查file.content_type
* 一旦你执行了 await file.read()，Python 读取文件的“光标（指针）”就走到了文件末尾。如果你这时候再去执行保存操作，你会存下来一个0字节的空文件 所以 可以在保存前先执行await file.seek(0)重置文件指针
* 真实业务中 常用UUID与时间戳进行重命名
* 在 HTTP 协议中，文件的身份标识叫 MIME Type (Content-Type)。它有严格的国际规范：
* 普通文本 (txt)：text/plain
* PDF 文档：application/pdf
* JPEG 图片：image/jpeg
* CSV 表格：text/csv
* 在文档问答 RAG等内容中至关重要
## 流式输出
* 用法：引入StreamingResponse 结合yield
* yield:生成器语法 如果出现在async def里 就是异步生成器的一部分
* 在SSE协议里 当media_type="text/event-stream" 格式为：data: 你的内容\n\n
* 大模型 AGENT工具中使用流式输出 前端与交互体验好 使得首字响应延迟（TTFT）短 用户体验好
* 当流式输出断连 Uvicorn会抛出asyncio.CancelledError异常 我们需要用try...finally块处理
## 算法
* 反转链表 相交链表 回文链表