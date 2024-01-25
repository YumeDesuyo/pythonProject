import os.path
import re

import requests

if __name__ == '__main__':
    # url = 'https://www.zhihu.com/special/all'
    url1 = 'https://www.zhihu.com/api/v4/news_specials/list?limit=10&offset=10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0'
    }
    params = {
        'limit': '10',
        'offset': '20',
    }
    page_text = requests.get(url=url1, headers=headers, params=params).text
    # 正则表达式，用于获取图片链接
    ex = '<div class="SpecialListCard-banner"><img src="(.*?)" alt=""/></div>'
    ex1 = '"banner": "(.*?)",'
    # 保存图片链接
    img_list = re.findall(ex1, page_text, re.S)
    print(img_list)
    # 创建图片保存的文件夹
    if not os.path.exists('ZhiHuimg'):
        os.mkdir('ZhiHuimg')

    for src in img_list:
        # 请求图片数据
        img_data = requests.get(url=src, headers=headers).content
        # 生成图片名称
        img_name = src.split('/')[-1]
        # 图片保存路径
        img_path = './ZhiHuimg/' + img_name
        # 保存图片
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name, '保存成功！！')
