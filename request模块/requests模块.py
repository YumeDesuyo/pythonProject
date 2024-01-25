# request模块可以模拟浏览器发请求
# 浏览器发请求步骤（request模块的编码流程）
# 1 指定url
# 2 发起请求
# 3 获取响应数据
# 4 持久化存储
# - 需求：爬取搜狗首页

import requests

if __name__ == "__main__":
    # 指定url
    url = 'https://csdcso.org/archive/'
    # 发起请求
    response = requests.get(url=url)
    # 获取响应数据
    page_text = response.text
    print(page_text)
    # 持久化存储
    with open('./gcg.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束')
