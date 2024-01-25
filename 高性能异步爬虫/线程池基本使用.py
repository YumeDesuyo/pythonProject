# import time
#
#
# def get_page(str):
#     print('正在下载' + str)
#     time.sleep(2)
#     print('下载成功' + str)
#
#
# name_list = ['aaa', 'bbb', 'ccc', 'ddd', ]
#
# start_time = time.time()
#
# for str in name_list:
#     get_page(str)
#
# end_time = time.time()
#
# print('%d serond' % (end_time - start_time))

# ================================================
import time
# 导入线程池模块对应的类
from multiprocessing.dummy import Pool

start_time = time.time()


def get_page(str):
    print('正在下载' + str)
    time.sleep(2)
    print('下载成功' + str)


name_list = ['aaa', 'bbb', 'ccc', 'ddd', ]

# 实例化一个线程池对象
pool = Pool(len(name_list))
# 将列表中每一个元素传递给get_page 进行处理
pool.map(get_page, name_list)

end_time = time.time()

print('%d second' % (end_time - start_time))
