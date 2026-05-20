from datetime import datetime

def get_current_time(city:str) -> dict:
    return{
        "city":city,
        "time":datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

def get_weather(city:str) -> dict:
    db = {
        "北京": {"weather": "晴", "temperature": "26°C"},
        "上海": {"weather": "阵雨", "temperature": "22°C"},
        "深圳": {"weather": "台风", "temperature": "28°C"}
    }

    result = db.get(city,{"weather": "未知", "temperature": "未知"})
    result["city"] = city
    return result

def calculate(expression:str) -> dict:
    try:
        result = eval(expression)
        return {"expression":expression,"result":result}
    except Exception as e:
        return {"error":f"计算失败：{str(e)}"}