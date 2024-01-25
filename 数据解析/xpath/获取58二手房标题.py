import requests
from lxml import etree
# 访问页面失败，需要验证码
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0'
    }
    url = 'https://zz.58.com/ershoufang/'
    page_text = requests.get(url=url, headers=headers).text
    # 实例化对象
    tree = etree.HTML(page_text)
    # 数据分析
    div_list = tree.xpath('//section[@class="list-main"]/div[@class="property-content"]')
    fp = open('./titles.txt', 'w', encoding='utf-8')
    fp.write(page_text + '\n')
    for div in div_list:
        print(div)
        title = div.xpath('./div[3]/h3/text()')[0]
        print(title)
        fp.write(title + '\n')