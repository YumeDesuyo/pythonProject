import json

import requests

if __name__ == '__main__':
    # 指定url
    url = 'http://www.haijun.online/api/articles'
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0'
    }
    # 发起请求
    count = input('please enter a number')
    params = {
        'current': count,
    }
    page_json = requests.get(url=url, params=params, headers=headers).json()
    # 数据持久化
    fp = open('网页采集json', 'w', encoding='utf-8')
    json.dump(page_json, fp=fp, ensure_ascii=False)

    print('over!!')
