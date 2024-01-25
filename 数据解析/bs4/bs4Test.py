from bs4 import BeautifulSoup

if __name__ == '__main__':
    fp = open('../asd.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, 'lxml')
    # print(soup)
    # soup.tagName 返回的是覅一次出现的tagName标签
    # print(soup.a)
    # find('tagName')等同于soup.tagName
    # print(soup.find('div'))
    # 层级选择
    # print(soup.find('div', class_='SpecialListCard-banner'))
    # select('某种选择器(id, class)')，返回的是一个列表
    # print(soup.select('.SpecialListCard-sections'))
    # 层级选择  ">"表示一个层级
    # print(soup.select('.SpecialListCard-sections > a'))
    # print(soup.select('.SpecialListCard-sections  a'))
    # 获取标签中的值text/string/get_text()
    # print(soup.select('div > p')[0].get_text())
    # 获取标签中属性值
    # print(soup.select('div > p a')[0] ['href'])
    
