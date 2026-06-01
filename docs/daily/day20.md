## 修day19bug
* 当前LangChain对照版只返回answer 并不返回sources
* 正式API版本仍以rag_service.py的原生实现为主 它更方便控制sources, score, preview
## 优化RAG项目
* RAG系统实际上分为离线数据管道和在线检索服务两个部分 全部实现才能闭环
* 在项目中 为了做并发性能和接口延迟优化 做了下面几个点：
* 对于向量数据库 大模型client等重量级对象 采用懒加载的单例模式 因为他们并不需要在每次请求时都保持独立状态 全局复用可以防止频繁建立连接
* 在高并发下 这样大大降低了磁盘IO与内存占用 防止OOM
* 我们现在就做lifespan:
* 使用lifespan功能 添加一个上下文管理器asynccontextmanager 保证在服务启动时就初始化Chroma 减少首响延迟
* 现在的热更新接口 实际工程中不能使用 因为复杂度过高O(N)
* 实际生产中：当增改时 采用增量更新 只计算这一片文档的chunks和embeddings 然后调用向量数据库的upsert接口
* 当必须全面清洗数据时 我们采用双端读写分离的思路 启动一个离线服务建立向量库B 在建立完成后 对向量库进行热切换
### 数据库
* conn:负责 connect commit close
* cursor速测execute fetchall（具体指令）
* SQL语句：建表：
```
CREATE TABLE IF NOT EXISTS query_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    query TEXT NOT NULL
)
```
* 增加数据:
```
INSERT INTO query_logs (query, answer, sources)
VALUES (?, ?, ?)
```
* 查
```
SELECT query, answer FROM query_logs WHERE latency_ms > 1000
```
* 事务：数据库保证 多步操作要么全部成功 要么全部撤销 使用conn.commit()
* 索引：用B+树查找
### ORM框架
* FastAPI中使用ORM：
```
# 1. 你先定义一个类
class User(BaseModel):
    id: int
    name: str
    age: int

# 2. 查询数据时，一句 SQL 都不用写！
users = session.query(User).filter(User.age > 18).all()
# 查出来直接是一个 User 类的对象！你可以直接 user.name 拿到名字！
```
* 业界使用SQLAlchemy与SQLModel
### 不同数据库对比
* MySQL 适合分布式的、多台服务器同时读写的复杂业务（比如淘宝订单）。
* Redis 是内存数据库，它的数据是存在内存条里的。它的强项是“极速读写”（用来做缓存、存会话），但它的弱项是“持久化和复杂查询”。
* SQLite 零配置、零依赖，对于单体 Python 应用是绝杀。
## 算法
* 前序和中序遍历创建二叉树：前序遍历确定根 中序遍历确定左右子树 算好数量进行切片递归
* 优化的话只需保存区间的四个点即可（主要这里用闭区间）
* LRU缓存：使用双向链表+哈希 为了防止分类讨论 使用幽灵头节点和尾节点
* 先写双向链表节点 再写辅助函数：头插和删除
* get注意Key不在时返回-1
* put注意key不在时 先创建新节点 再写进二叉树 再头插
* 此时如果capacity超载 先拿到老节点 然后删哈希表 最后删老节点
* 这两道题要反复复习！