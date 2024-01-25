from lxml import etree

if __name__ == '__main__':
    tree = etree.parse('../asd.html')
    # r = tree.xpath('/html/body/div')
    # r = tree.xpath('/html//div')
    # r = tree.xpath('//div')
    # r = tree.xpath('//div[@class="class_one"]')
    # r = tree.xpath('//div[@class="class_two"]/p[2]')
    r = tree.xpath('//div[@class="class_two"]/p//text()')[0]
    print(r)
