import os.path

import requests
from lxml import etree

if __name__ == '__main__':
    url = 'https://csdcso.org/archive/05%20Q%E4%BA%BA%E7%89%A9%E4%B8%8E%E7%8E%BB%E7%92%83%E7%AA%97/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0'
    }
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML()
    li_list = tree.xpath('//div[@class="mainrow"]/li')
    # 创建文件夹用于保存图片
    if not os.path.exists('./4k'):
        os.mkdir('./4k')
    for li in li_list:
        img_src = 'https://pic.netbian.com/' + li.xpath('./a/img/@src')[0]
        img_name = li.xpath('./a/img/@alt')[0].encode('iso-8859-1').decode('gbk') + '.jpg'
        # print(img_src, img_name)
        img_data = requests.get(url=img_src, headers=headers).content
        img_path = 'C:/Users/32091/Desktop/图片/' + img_name
        with open(img_path, 'wb') as fp:
            fp.write(img_data)
            print(img_name + '保存成功')
