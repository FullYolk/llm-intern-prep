from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class GraphState(TypedDict):
    question:str
    category:str
    answer:str

def class_question_func(state:GraphState):
    if "FastAPI" in state["question"] or "Agent" in state["question"]:
        return {"category": "tech"}
    return {"category": "daily"}

def technical_answer_func(state:GraphState):
    return {"answer": f"这是一个技术问题，我的回答是：{state['question']} 是一个很好的技术。"}

def daily_answer_func(state:GraphState):
    return {"answer": f"这是一个日常问题，我的回答是：今天天气不错！"}

def route_func(state:GraphState):
    return state["category"]

workflow = StateGraph(GraphState)

workflow.add_node("classify", class_question_func)
workflow.add_node("techno",technical_answer_func)
workflow.add_node("daily_answer", daily_answer_func)

workflow.add_edge(START,"classify")
workflow.add_edge("techno",END)
workflow.add_edge("daily_answer", END)

workflow.add_conditional_edges(
    "classify",
    route_func,
    {
        "tech":"techno",
        "daily":"daily_answer"
    }
)

app = workflow.compile()

result = app.invoke({"question":"今天吃什么？","category":"","answer":""})

print(result)


