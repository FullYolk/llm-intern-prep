import httpx
def get_test():
    response = httpx.get("https://httpbin.org/get",params={"user": "beihang_cs","level": 99})
    print(response.status_code)
    print(response.json())

def post_test():
    response = httpx.post("https://httpbin.org/post",json={"message":"Hello llm","model": "GPT4"})
    print(response.status_code)
    print(response.json())

def timeout_test():
    response = httpx.get("https://httpbin.org/get",params={"user": "beihang_cs","level": 99},timeout=0.00000001)
    print(response.status_code)
    print(response.json())

def except_test():
    try:
        response = httpx.get("https://httpbin.org/status/404",params={"user": "beihang_cs","level": 99})
        print(response.status_code)
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        print("请求失败 状态码是：",e.response.status_code)

def main():
    get_test()
    post_test()
    # timeout_test()
    except_test()
if __name__ == "__main__":
    main()
