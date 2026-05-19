## 有无system实验结果：
PS D:\llm-intern-prep> & C:\Users\FullYolk\AppData\Local\Python\pythoncore-3.14-64\python.exe d:/llm-intern-prep/practice/llm/day09_prompt_basics/prompt_experiments.py
FastAPI 是一个现代、高性能的 **Python Web 框架**，专为构建 **APIs**（特别是 RESTful API）而设计。它由 Sebastián Ramírez 开发，于 2018 年开源，迅速成为 Python 生态中备受瞩目的框架之一。

---

### 核心特点

1. **极快的性能**  
   FastAPI 基于 **Starlette**（异步 Web 框架）和 **Pydantic**（数据验证库），底层使用 **ASGI**（异步服务器网关接口），性能可与 **Node.js** 和 **Go** 相媲美，是 Python 最快的 Web 框架之一（仅低于纯异步框架如 sanic）。

2. **自动生成交互式 API 文档**  
   利用 **OpenAPI**（原 Swagger）规范，FastAPI 会自动为你的 API 生成两个文档界面：
   - **Swagger UI**（`/docs`）：可在线测试每个端点。
   - **ReDoc**（`/redoc`）：更清晰、更强大的文档展示。

3. **基于 Python 类型提示（Type Hints）**  
   你只需在函数参数和返回类型上使用 Python 标准类型注释（如 `str`、`int`、`List[str]`、自定义 Pydantic 模型等），FastAPI 就会自动：
   - 进行请求数据验证（类型、范围、格式等）。
   - 自动生成文档中的 Schema。
   - 提供编辑器自动补全和类型检查。

4. **异步支持（Async/Await）**  
   原生支持异步编程，适合高并发 I/O 密集型应用（如数据库查询、第三方 API 调用）。当然也兼容同步代码。

5. **数据验证与序列化**  
   通过 Pydantic 模型，可轻松定义请求体、响应体，并自动校验和转换数据。错误信息清晰、易于调试。

---

### 典型工作流程

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
async def create_item(item: Item):
    return {"message": f"Item '{item.name}' created with price {item.price}"}
```

启动后访问 `/docs`，即可看到自动生成的 API 文档，并可直接在页面中测试。

---

### 适用场景

- 构建 RESTful / GraphQL API
- 微服务架构
- 高并发 Web 服务（聊天、实时推送等）
- 需要快速原型开发且要求性能的项目
- 与前端（React、Vue 等）无缝配合

---

### 快速上手

安装：  
```bash
pip install fastapi
# 服务器（推荐 uvicorn）
pip install uvicorn
```

运行：  
```bash
uvicorn main:app --reload
```

访问：  
- API 测试：`http://127.0.0.1:8000/docs`
- 交互式文档：`http://127.0.0.1:8000/redoc`

---

### 总结

**FastAPI = 高性能 + 自动文档 + 类型安全 + 异步支持**。它让 Python 开发者能以接近静态语言的方式编写接口，同时获得接近原生速度的性能，非常适合现代 Web 后端开发。
以下是第二则
1. **基于 Python 的现代 Web 框架**：专为构建 API 设计，支持异步，性能接近 Node.js/Go。  
2. **自动生成交互式文档**：通过类型提示自动生成 OpenAPI 文档（Swagger UI/ReDoc）。  
3. **依赖注入与数据校验**：内置 Pydantic 模型校验，简化请求/响应验证与错误处理。  

```python
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root(): return {"Hello": "World"}
```
PS D:\llm-intern-prep> 

## 上下文学习实验结果：
PS D:\llm-intern-prep> & C:\Users\FullYolk\AppData\Local\Python\pythoncore-3.14-64\python.exe d:/llm-intern-prep/practice/llm/day09_prompt_basics/prompt_experiments.py
意图：查询高铁票

实体：
- 时间：明天
- 出发地：北京
- 目的地：上海
- 交通工具：高铁票
以下是第二则
意图：查高铁票 | 实体：时间=明天，出发地=北京，目的地=上海
## 温度测试结果:
PS D:\llm-intern-prep> & C:\Users\FullYolk\AppData\Local\Python\pythoncore-3.14-64\python.exe d:/llm-intern-prep/practice/llm/day09_prompt_basics/prompt_experiments.py
1. **Pawsome "PEP-8" Whiskers**  
   - 口头禅：“喵？你的代码缩进用的是 Tab 还是毛球？——建议你再去读一遍《Python 之禅》。”

2. **SyntaxError "Pycat" Purrington**  
   - 口头禅：“喵嗷！你这段代码居然没有语病……哦不，语法错误，我简直想给它一个肉垫点赞。”

3. **Catplotlib Overflow**  
   - 口头禅：“喵，虽然我不会跑数据，但我能跑酷——记住，`import this` 比 `import tuna` 更重要！”
以下是重跑0.0
1. **递归喵**（Recursive Meow）  
2. **Try-Except 猫**（Catch 喵）  
3. **None 猫**（Meow None）  

**口头禅**：“喵了个喵！你又忘了冒号？看我用爪子帮你补上——啪！”
以下是0.7
1. **PEP 8 喵** —— 一只强迫症晚期的猫，写代码必须先格式化，连毛都要按缩进舔。  
2. **递归喵** —— 追自己尾巴追到 Stack Overflow，号称“没有尾递归优化也能无限喵”。  
3. **None 喵** —— 口头禅是“我什么都没做，但你的程序炸了”，实际是偷偷把变量赋成了 `None`。  

**口头禅**：  
“喵～ 你报错，我背锅，最后还得 `pip install 小鱼干` 才能修。”
以下是1.3
好的，以下是三只“会写 Python 的猫”的名字和它们的口头禅：

1. **喵 import 鱼**  
   （日常操作：先 import 鱼，再 print(“喵”)）

2. **Pawthon**  
   （Paw + Python，踩键盘写代码的专精猫）

3. **递归喵 (Recursive Meow)**  
   （永远在调用自己，直到 stack overflow 或小鱼干出现）

**口头禅：**  
> **“喵了个 SyntaxError！你的括号不对称，让我用尾巴帮你补一个。”**
试一下2.0
好的，这里是为一只会写 Python 的猫准备的三个搞笑名字和一句口头禅：

### 搞笑名字

1. **抓 Bug 的汤姆**（Tom the Bug Catcher，致敬经典，但改成了修 bug 的猫）  
2. **递归喵**（Recursive Meow，因为它解决问题的方式总是“喵自己”）  
3. **缩进狂魔·键盘破坏者**（Indent Monster & Keyboard Destroyer，猫爪拍空格和 Tab 的后果）

### 口头禅

> **“喵～代码跑不动？让我看看……哦，你少了一个冒号，还不缩进，是想让 Python 气炸吗？”**
## 输出格式结果:
PS D:\llm-intern-prep> & C:\Users\FullYolk\AppData\Local\Python\pythoncore-3.14-64\python.exe d:/llm-intern-prep/practice/llm/day09_prompt_basics/prompt_experiments.py
- 简洁易读的语法，降低学习成本
- 丰富的标准库与第三方生态
- 跨平台兼容性与良好的可移植性