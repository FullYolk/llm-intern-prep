tools = [
    {
        "type":"function",
        "function": {
            "name":"get_weather",
            "description":"获取指定城市的天气状况，当用户询问天气时调用该工具",
            "parameters":{
                "type":"object",
                "properties":{
                    "city":{
                        "type":"string",
                        "description":"城市名称，例如：北京，上海"
                    }
                },
                "required":["city"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "获取指定城市的当前时间，当用户询问时间时调用此工具。",
            "parameters": {
                "type":"object",
                "properties":{
                    "city":{
                        "type":"string",
                        "description":"城市名称，例如：北京，上海"
                    }
                },
                "required":["city"]
            }
            
        }
    },

    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "计算数学表达式的结果。当用户需要进行四则运算时调用此工具。",
            "parameters": {
                "type":"object",
                "properties":{
                    "expression":{
                        "type":"string",
                        "description":"合法的数学表达式 例如3+5"
                    }               
                },
                "required":["expression"]
            }
        }
    }
]