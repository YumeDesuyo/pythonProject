import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.0.0'
}
img_src = 'https://pic.netbian.com/'
img_name = 'whee.jpg'
# print(img_src, img_name)
img_data = requests.get(url=img_src, headers=headers).content
img_path = 'C:/Users/32091/Desktop/图片/' + img_name
with open(img_path, 'wb') as fp:
    fp.write(img_data)
    print(img_name + '保存成功')
