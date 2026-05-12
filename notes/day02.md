 Pythonic 的终极解决绝招（面试必考）
如果你以后遇到“要删除列表里符合条件的多个元素”的场景，Python 有两种标准企业级写法：

绝招 1：遍历原列表的“切片拷贝”（用 [:]）

<PYTHON>
for s in students[:]:  # 加上 [:] 代表我们遍历的是一个临时克隆出来的影子数组
    if s["name"] == "Bob":
        students.remove(s) # 在原数组上随便删，影子数组的指针不会乱
绝招 2：列表推导式全覆盖（最推荐，也是速度最快的）
不要想着“删除不想要的”，而是“把想要的挑出来，覆盖原列表”：

<PYTHON>
# [:] 切片赋值操作，代表把右边新生成的列表内容，原封不动地塞回给原来的 students 内存地址
students[:] = [s for s in students if s["name"] != "Bob"]

1. 集合 set 与去重
C 语言思维：去重需要两层 for 循环，或者先排序再双指针，时间复杂度 O(n²) 或 O(nlogn)。
Python 思维：set 的底层是哈希表。把一个 List 扔进 set()，瞬间去重（O(n)），再用 list() 包装回来即可。
2. 匿名函数 lambda 与自定义排序
场景：如果你有一个装满字典的列表 [{"name": "A", "score": 90}, {"name": "B", "score": 80}]，你想按 score 排序。
武器：sorted(数据, key=排序规则函数, reverse=True)。
什么是 lambda：它就是一个不需要起名字的、只有一句话的微型函数。
原本你需要写：def get_score(student): return student["score"]
用 lambda 只要写：lambda student: student["score"]
连起来就是：sorted(students, key=lambda x: x["score"], reverse=True)
3. 列表推导式 (List Comprehension)
企业级规范：在 Python 中，如果只是为了过滤数组或对每个元素做简单操作，严禁写传统的 4 行 for 循环 + append，必须用一行“推导式”搞定。
语法：[对元素的操作 for 元素 in 数组 if 过滤条件]
例子：要把 [1, 2, 3] 全变成平方：[x*x for x in nums]。
4. 拉链函数 zip
场景：你有两个数组，一个是表头 ["name", "age"]，一个是数据 ["Alice", 20]，你想把它们一一对应拼起来。
武器：zip(list1, list2) 就像拉链一样，把对应位置的元素打包成元组 ("name", "Alice")。如果配合 dict()，瞬间就能把两个数组变成一个字典！
坑点：如果两个数组长度不一样，zip 会极其无情地以短的那个为准，多出来的直接丢弃。
5. json 序列化与反序列化
为什么极其重要：不管你以后调 OpenAI API，还是做 FastAPI 接口，网络传输的数据格式 100% 都是 JSON。在 Python 中，JSON 和 字典（dict）长得几乎一模一样，但 JSON 是字符串 (str)，字典是内存对象 (dict)。
转换：
字典 -> 存入文件：json.dump(数据, 文件句柄)
文件 -> 读成字典：json.load(文件句柄)
(如果是纯内存字符串转换，用 json.dumps() 和 json.loads()，多了一个 s 代表 string)。
中文不乱码外挂：json.dump(..., ensure_ascii=False, indent=2)（indent=2 会自动帮你缩进排版，极其美观）。