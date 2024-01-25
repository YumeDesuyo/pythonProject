import requests

if __name__ == '__main__':
    # 指定url
    url = 'https://pic4.zhimg.com/100/v2-7fcac84fcec75e5403d34f7c3b8845eb_hd.png'
    # content返回的是二进制形式的图片数据
    img_data = requests.get(url=url).content
    with open('zhihu.png', 'wb') as fp:
        fp.write(img_data)
