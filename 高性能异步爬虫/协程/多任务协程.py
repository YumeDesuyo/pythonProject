import asyncio
import time


# 定义一个阻塞方法
async def request(url):
    print('正在下载：' + url)
    await asyncio.sleep(2)
    print('下载完成：' + url)


# 定义url合集
urls = ['www.baidu.com', 'www.baidu.com', 'www.baidu.com']

# 定义task任务合集
tasks = []

for url in urls:
    c = request(url)
    task = asyncio.ensure_future(c)
    tasks.append(task)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
