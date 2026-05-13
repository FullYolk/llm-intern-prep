* 不要用len,list,dict这种Python内置名字当变量名
## Pydantic基础
* BaseModel与DataClass的区别：
* 自动类型转换
* 严格的类型校验和拦截
* 序列化与反序列化：反序列化：Student(**json_dict) 将JSON转为对象 序列化：student.model_dump()：将对象转为字典 方便存入数据库
* BaseModel实际上是用RUST重写底层校验逻辑 使用MetaClass动态生成校验树
* Optional[int] 意为：该字段要么是int 要么是None
* Pydantic中默认给可变对象：tags:list = Field(default_factory=list)
* Field的常用约束：gt ge lt le min_length max_length pattern(正则表达式) default_factory=list/dict(数据工厂) description=""(该字段的含义)
## 小迭代toy项目
* add_student返回bool 能够判断是否添加成功 更加便于对齐接口与后续调用
* 进行重名检查 有效提高安全性和正确性
* 在toy项目中养成习惯 为后续开发做准备
* 对齐接口后 在FastAPI中依然可复用
## 算法：
* 有效括号匹配：判断栈空
* 三数之和：固定一个数+双指针 记得去重（排序后遇到相同跳过） 若N数之和 固定N-2个数再双指针 + 剪枝即可