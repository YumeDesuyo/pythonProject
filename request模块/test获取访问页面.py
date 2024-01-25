import requests

if __name__ == '__main__':
    # UA伪装：将对应的请求载体身份标识伪装成一款浏览器
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0'
    }
    url = 'https://cn.bing.com/search'
    # 将请求参数封装到字典中
    keyword = input('请输入关键词：')
    param = {
        'q': keyword
    }
#     对指定的url发起请求中是携带参数的
response = requests.get(url=url, params=param, headers = headers)
page_text = response.text
filename = keyword + '.html'
with open(filename, 'w', encoding='utf-8') as fp:
    fp.write(page_text)
print(filename, '保存成功！！')
