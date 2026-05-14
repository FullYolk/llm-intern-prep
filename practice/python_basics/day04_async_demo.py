import time
import asyncio
def sync_task(name):
    print(f"[同步]任务{name} 开始工作！")
    time.sleep(2)
    print(f"[同步]任务{name} 工作完成！")

def run_sync():
    start = time.perf_counter()
    sync_task("A")
    sync_task("B")
    sync_task("C")
    print(f"同步总耗时：{time.perf_counter()-start:.2f}秒\n")

async def async_task(name):
    print(f"[异步]任务{name} 开始工作！")
    await asyncio.sleep(2)
    print(f"[异步]任务{name} 工作完成！")

async def run_async():
    start = time.perf_counter()
    await asyncio.gather(
        async_task("A"),
        async_task("B"),
        async_task("C")
    )
    print(f"异步总耗时：{time.perf_counter()-start:.2f}秒\n")

def main():
    print("开启同步测试")
    run_sync()
    print("开启异步测试")
    asyncio.run(run_async())

if __name__ == "__main__":
    main()