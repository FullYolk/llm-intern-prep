import json
import os
from dotenv import load_dotenv
from openai import OpenAI
from tools import get_weather,get_current_time,calculate
from tool_schemas import tools
import llm_client
from llm_client import MODEL_NAME
#路由映射表:

available_tools = {
    "get_weather":get_weather,
    "get_current_time":get_current_time,
    "calculate":calculate
}

client = llm_client.get_client()

def run_conversation():
    messages = [{"role":"user","content":"今天上海天气怎么样？"}]
    print(f"用户问题:{messages[0]['content']}")
    print("等待模型决策...")
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    print("模型原始回复如下:")
    print(message)
    print("原始回复结束")

    messages.append(message)

    if message.tool_calls:
        print("模型决定调用工具!")
        for tool_call in message.tool_calls:
            name = tool_call.function.name
            try:
                arguments = json.loads(tool_call.function.arguments)
            except json.JSONDecodeError as e:
                function_result = {"error": f"参数JSON解析失败{str(e)}"}
            function_to_call = available_tools.get(name)
            if function_to_call is None:
                function_result = {"error": f"未知工具{name}"}
            else:
                function_result = function_to_call(**arguments)
            print(f"函数执行结果:{function_result}")
            res_str = json.dumps(function_result,ensure_ascii=False)
            messages.append({"role":"tool","tool_call_id":tool_call.id,"content":res_str})
        reply = client.chat.completions.create(model=MODEL_NAME,messages=messages)
        answer = reply.choices[0].message
        print("模型最终回答如下：")
        print(answer.content)
        print("回答结束")
    else:
        print("模型没有调用工具 它直接回答了！")
        print(message.content)
            
def main():
    run_conversation()

if __name__ == "__main__":
    main()