## 完成day01遗留问题
* 修改规范命名
* 注释
* 加import
## 做了8个python语法drills
* 列表去重：套一层set
* 统计词频：利用dict的get函数（key,返回默认值）
* 排序：lambda匿名函数：直接写标准即可 reverse = True默认降序
* 列表推导式：s()结果 for s in students if 条件
* 使用enumerate遍历同时拿到下标和内容（返回值为元组）
* 合并List为dict 直接使用dict(zip(li)) 一一对应 以短的截断
* 读写json:使用with open读写 json.dump json.load
## 完善小toy管理系统
* 使用os.path.join()拼接路径
* 注意引号冲突
* 字典的遍历时删除：两个相邻的相同键 会漏掉元素不删除
* 解决方案 1.使用 for s in students[:]（影子数组） 2.切片式赋值： students[:] = [s for s in students if s["name"] != "Bob"]
## 两个Python OOP demo
* Python类：self为固定第一个参数
* 构造函数__init__ 还需编写__str__ to_dict等
* 没有new关键字 直接赋值
* 自适应格式
* dataclass:自动初始化构造函数和一些其他函数
* 同时有三点好处：节省内存 做frozen可变后直接只读+强哈希能力 防止出现“可变默认值”
* 可变默认值：在 Python 中，函数的“默认参数”是在【函数被定义（def）的那一瞬间】计算并分配内存的，而不是在【函数被调用】时分配的！
* 因此 参数中有dict/list时 内存会被分配在同一地址
* “可变默认参数陷阱”必须且仅当你在参数列表里使用了等号 =，并且右边直接给了一个 [] 或 {} 时才会触发。
* 譬如dfs遍历：应写成def dfs(node, path=None):
    if path is None:
        path = []
    # ...
* 写普通类时 必须写成：class Student:
    def __init__(self, name: str, tags: list = None):
        if tags is None:
            self.tags = []  # 重点：这样写，每次实例化跑到这里时，都会临时新建一块内存！
        else:
            self.tags = tags
* 但dataclass提供了：tags: list = field(default_factory=list)
* 在单纯建存数据的类时 应使用dataclass更加简便 但在遇到复杂业务逻辑时 还是应该使用class
## 算法：
最长连续序列：利用set的O（1）复杂度查找
移动0：快慢针
盛最多水：左右针