import logging
import httpx
import time

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def fetch_data():
    logging.info("准备向目标网站发起请求")
    start_time = time.perf_counter()
    response = httpx.get("https://httpbin.org/get",params={"user": "beihang_cs","level": 99})
    end_time = time.perf_counter()
    usedtime = end_time - start_time
    if response.status_code == 200:
        logging.info(f"成功访问了！耗时为：{usedtime}")
    try:
        response = httpx.get("https://httpbin.org/404",params={"user": "beihang_cs","level": 99})
        response.raise_for_status()
    except httpx.HTTPStatusError as e:
        logging.error(f"请求失败了！状态码是:{e.response.status_code}")

def main():
    fetch_data()

if __name__ == "__main__":
    main()