import requests

if __name__ == '__main__':
    # 指定url
    url_post = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0'
    }
    # post请求参数处理（同get一样）
    data = {
        'kw': 'cat'
    }
    response = requests.post(url=url_post, data=data, headers=headers)
    dic_obj = response.json()
    print(dic_obj)
