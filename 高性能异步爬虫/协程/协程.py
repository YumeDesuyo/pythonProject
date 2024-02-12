import asyncio


async def request(url):
    print('正在请求url:' + url)
    print('请求成功:' + url)
    return url


# async修饰的函数，调用后返回一个协程对象
c = request('www.baidu.com')


# # 创建一个事件循环对象
# loop = asyncio.get_event_loop()
#
# # 将循环对象注册到loop中，并启动loop
# loop.run_until_complete(c)

# # task的创建
# loop = asyncio.get_event_loop()
# # 基于loop创建task对象
# task = loop.create_task(c)
#
# print(task)
#
# # 将task任务注册到loop中
# loop.run_until_complete(task)
# print(task)


# # future的使用
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)
# print(task)
# loop.run_until_complete(task)
# print(task)

# # 定义回调函数
# def callback_fun(task):
#     print(task.result())
#
#
# # 绑定回调
# loop = asyncio.get_event_loop()
# task = loop.create_task(c)
# task.add_done_callback(callback_fun)
# loop.run_until_complete(task)
