import asyncio


# async修饰的函数，调用后返回一个协程对象
async def request(url):
    print('正在请求url:' + url)
    print('请求成功' + url)


c = request('www.baidu.com')

# # 创建一个时间循环对象
# loop = asyncio.get_event_loop()
#
# # 将循环对象注册到loop中，然后启动loop
# loop.run_until_complete(c)

# # task的创建
# loop = asyncio.get_event_loop()
# task = loop.create_task(c)
#
# print(task)
#
# # 将task任务注册到loop中
# loop.run_until_complete(task)
# print(task.result())


# # future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)


# 绑定回调
