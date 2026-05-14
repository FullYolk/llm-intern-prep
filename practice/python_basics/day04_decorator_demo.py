import time
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s %(message)s]"
)

def time_logger(func):
    def wrapper(*args, **kwargs): #接收一切可能的参数
        start = time.perf_counter()
        result = func(*args, **kwargs) #传参
        end = time.perf_counter()
        usedtime = end - start
        logging.info(f"{func.__name__}执行耗时：{usedtime:.4f}")
        return result
    return wrapper

@time_logger
def complex_calculation():
    logging.info("假装正在进行复杂的计算")
    time.sleep(1.5)
    logging.info("计算完成")

def main():
    complex_calculation()

if __name__ == "__main__":
    main()