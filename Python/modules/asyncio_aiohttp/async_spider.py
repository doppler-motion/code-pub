import asyncio
import time

import aiohttp

urls = [f"https://www.cnblogs.com/sitehome/p/{page}" for page in range(1, 50 + 1)]


# 协程的写法
async def async_craw(url):
    print(f"craw url: {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            result = await resp.text()
            print(f"craw url: {url}, {len(result)}")


loop = asyncio.get_event_loop()  # 获取超级循环

tasks = [loop.create_task(async_craw(url)) for url in urls]  # 创建任务

start = time.time()
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print(f"async cost time : {end - start}")



