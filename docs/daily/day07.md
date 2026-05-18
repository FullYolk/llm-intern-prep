## 修day6bug
* 中间件最好用logging
* 文件保存要防路径穿越 用UUID防范 同时还能解决并发覆盖问题
* content_type不能完全信任 真实系统还会 检查后缀 文件大小 文件头magic bytes 做病毒扫描
* status_code一般语义：| 状态码 | 含义 |
|---|---|
| 200 | 请求成功 |
| 201 | 创建资源成功 |
| 204 | 成功但无返回体 |
| 400 | 请求参数错误 |
| 401 | 未登录 |
| 403 | 无权限 |
| 404 | 资源不存在 |
| 500 | 服务端错误 |
## Docker运行Redis 常用命令
- docker pull redis 拉取镜像
- docker run -d --name my-redis -p 6379:6379 redis 启动容器 -d后台运行 -p端口映射 宿主机端口:容器内端口
- docker ps 列出容器信息
- docker exec -it my-redis redis-cli exec 进入容器 -it:交互式输入 分配伪终端 redis-cli具体命令
- docker stop my-redis
- docker start my-redis
- docker rm my-redis 删除
* Redis的优势: 跨进程共享 断电不丢数据 有List Expire等高阶数据结构
* 在Agent开发中 存储聊天历史 做API限流 缓存结果 Redis 是内存数据库，速度快；支持 RDB/AOF 持久化，开启后可以在重启后恢复数据。
## Git与Linux命令复习
* git merge:合并 生成全新的提交 绝对安全 git merge: 合并分支，通常不会改写已有历史；可能产生 merge commit，也可能 fast-forward。
* git rebase：变基 会篡改历史 直接插到main分支的最顶端 永远不要在公共分支上rebase
* git reset:直接消失commit 没Push时使用 保持历史干净
* git revert:生成全新的commit 追加历史
pwd
ls
ls -la
find . -name "*.py"
find . -name "*.md"
grep -R "FastAPI" .
## 算法
和为K的子数组 前缀和+哈希