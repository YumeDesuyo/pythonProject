import json

import requests

if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0'
    }
    data = {
        'cname': '',
        'pid': '',
        'keyword': '北京',
        'pageIndex': '1',
        'pageSize': '10',
    }
    response = requests.post(url=url, data=data, headers=headers)
    list_data = response.text
    with open('./kfc.json', 'w', encoding='utf-8') as fp:
        fp.write(list_data)
    # fp = open('./kfc.json', 'w', encoding='utf-8')
    # json.dump(list_data, fp=fp, ensure_ascii=False)
    print(list_data)
    print('over!!')
