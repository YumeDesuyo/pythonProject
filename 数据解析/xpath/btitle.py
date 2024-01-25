import requests
from lxml import etree

url = 'http://awcoc.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0'
}
page_text = requests.get(url=url, headers=headers).text
tree = etree.HTML(page_text)
result = tree.xpath('//span[@id="verImg"]/text()')

print(result)
# with open('./videotitle.txt', 'w', encoding='utf-8') as fp:
#     fp.write(video_title)
