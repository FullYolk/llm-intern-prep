## day4错误修补
* 装饰器加functools.wraps是好习惯
* timeout最好加入异常处理
## FastAPI入门
* "FastAPI 是一个基于 Starlette 的高性能 Web 框架，并深度集成了Pydantic，天然支持 ASGI(Asynchronous Server Gateway Interface) 协议和异步请求处理的现代 Web 框架。
第一，它天生支持 async/await，处理大模型流式输出这种 I/O 密集型高并发场景极具优势。
第二，它深度整合了 Pydantic，基于 Python 的类型提示（Type Hinting）在边缘层自动完成数据的序列化和校验，极大减少了脏数据引发的崩溃。
第三，它完全遵循 OpenAPI 规范，能在代码编写的同时全自动生成强交互的 Swagger 接口文档，大幅降低了前后端联调的成本。"
操作过程：
python -m venv .venv
.venv\Scripts\activate
uvicorn main:app --reload （文件名 实例化名 每次修改代码自动重启）
* 使用venv进行环境隔离：
* venv:轻量级 python自带 只隔离纯净的依赖库
* conda:中量级 跨语言 可以隔离不通过版本的解释器与C/C++依赖
* Docker:系统及隔离 操作系统级别的虚拟化
* FASTAPI的路由注册本质是装饰器 通过路由分发 精准找到对应函数进行处理
* 用Swagger文档做前后端契约
* @app.get():取数据 查询
* @app.post()：递交数据/存数据 创建
* @app.delete():删除数据
* @app.put():全量替换 ##本质上都是HTTP方法语义 不是语法规定
* @app.patch():局部修改
* Path参数（路径参数）：@app.get("/todos/{todo_id}")中的{todo_id} 是直接嵌在网址里的变量 用于精确定位 只要URL外有{}且函数参数中也有
* Query参数(查询参数)：是跟在网站的?后面的参数 在def get_todos(completed: bool | None = None):中 由于没写在URL路径中 会自动识别为Query参数 用于筛选，过滤，分页
* Body参数（Pydantic请求体参数）:传入Pydantic模型后自动读取Body数据 用于提交复杂表单
* Header参数 用于存放不能放在URL中 也不适合放在Body中的内容 如身份验证Token 设备型号等
* Form参数（表单） 传统的网页登陆框 不发JSON 发老式表单格式
* File参数：文件上传
* FastAPI 会根据函数参数位置 + 类型注解 + 是否在路径里出现来推断参数来源。
* schemas.py是约定俗成的 所有继承于Pydantic中BaseModel类的类都在次定义

## 算法
* 字母异位词分组：定长滑动窗口
* 最小栈：维护两个栈 空间换时间
* 接雨水：双指针 维护left_max与right_max 确认短板后计算头上的雨水
