import llm_client
from llm_client import MODEL_NAME

def experiment_1_system_prompt():
    messages1 = []
    messages1.append({"role":"user", "content":"解释一下FastAPI是什么"})
    client = llm_client.get_client()
    response = client.chat.completions.create(model=MODEL_NAME,messages=messages1,temperature=0.7)
    content = response.choices[0].message.content
    print(content)
    print("以下是第二则")
    messages2 = [{"role": "system", "content": "你是一个面向北航计算机专业大二学生的严谨助教。请用极其简练的语言解释，必须分为 3 个点，并附带一行核心代码示例。不要废话。"}, {"role": "user", "content": "解释一下 FastAPI 是什么"}]
    response2 = client.chat.completions.create(model=MODEL_NAME,messages=messages2,temperature=0.7)
    content2 = response2.choices[0].message.content
    print(content2)

def experiment_2_few_shot():
    messages1 = []
    messages1.append({"role":"user", "content":"提取这句话中的实体和意图：帮我查一下明天北京去上海的高铁票"})
    client = llm_client.get_client()
    response = client.chat.completions.create(model=MODEL_NAME,messages=messages1,temperature=0.7)
    content = response.choices[0].message.content
    print(content)
    print("以下是第二则")
    messages2 = [{"role": "user", "content": "帮我点一杯冰美式"},{"role": "assistant", "content": "意图：点餐 | 实体：冰美式"},{"role": "user", "content": "今天天气怎么样"},{"role": "assistant", "content": "意图：查天气 | 实体：无"},{"role": "user", "content": "帮我查一下明天北京去上海的高铁票"}]
    response2 = client.chat.completions.create(model=MODEL_NAME,messages=messages2,temperature=0.7)
    content2 = response2.choices[0].message.content
    print(content2)

def experiment_3_temperature():
    messages1 = []
    messages1.append({"role":"user", "content":"为一个会写 Python 的猫起 3 个搞笑的名字，并给出一句它的口头禅。"})
    client = llm_client.get_client()
    response = client.chat.completions.create(model=MODEL_NAME,messages=messages1,temperature=0.0)
    content = response.choices[0].message.content
    print(content)
    print("以下是重跑0.0")
    response = client.chat.completions.create(model=MODEL_NAME,messages=messages1,temperature=0.0)
    content = response.choices[0].message.content
    print(content)
    print("以下是0.7")
    response = client.chat.completions.create(model=MODEL_NAME,messages=messages1,temperature=0.7)
    content = response.choices[0].message.content
    print(content)
    print("以下是1.3")
    response = client.chat.completions.create(model=MODEL_NAME,messages=messages1,temperature=1.3)
    content = response.choices[0].message.content
    print(content)
    print("试一下2.0")
    response = client.chat.completions.create(model=MODEL_NAME,messages=messages1,temperature=2.0)
    content = response.choices[0].message.content
    print(content)

def experiment_4_format_constraint():
    messages1 = []
    messages1.append({"role":"user", "content":"请列出 Python 的 3 个核心优点。请只输出三条带 '-' 的 bullet 列表，绝对不要写任何开场白、解释性废话或结尾。务必避免所有bullet列表外的额外字符。"})
    client = llm_client.get_client()
    response = client.chat.completions.create(model=MODEL_NAME,messages=messages1,temperature=0.7)
    content = response.choices[0].message.content
    print(content)

    

def main():
    experiment_4_format_constraint()
if __name__ == "__main__":
    main()