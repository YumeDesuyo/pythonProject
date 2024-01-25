import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'http://shici.yiduiyi.net.cn/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0'
    }
    page_text = requests.get(url=url, headers=headers).text
    # 实例化BeautifulSoup对象，将页面数据加载到对象中
    soup = BeautifulSoup(page_text, 'lxml', from_encoding='utf-8')
    #  解析章节标题和详情页url
    li_list = soup.select('.book-mulu > ul > li')
    # 创建保存小说的文件
    fp = open('./三国.txt', 'w', encoding='utf-8')
    for li in li_list:
        # 获取标题
        title = li.a.string.encode('iso-8859-1').decode('utf-8')
        # 获取详情页url
        detail_url = li.a['tppabs']
        # 向详情页发请求并持久化存储
        detail_response = requests.get(url=detail_url, headers=headers)
        detail_text = detail_response.content.decode('utf-8')
        detail_soup = BeautifulSoup(detail_text, 'lxml', from_encoding='utf-8')
        content = detail_soup.find('div', class_='chapter_content').getText()
        fp.write(title + '：' + content + '\n')
        print(title + '保存成功')
