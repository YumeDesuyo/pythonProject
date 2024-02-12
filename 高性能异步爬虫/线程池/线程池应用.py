import random
import re

import requests
from lxml import etree
from multiprocessing.dummy import Pool

# 定义url集合
urls = []


# 定义下载视频的方法
def download_video(urls):
    url = urls['url']
    filename = urls['name']
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        print(f"downloading {filename}")
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        print(f"Video downloaded successfully to {filename}")
    else:
        print(f"Failed to download video. HTTP status code: {response.status_code}")


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

url = 'https://www.pearvideo.com/panorama'
page_text = requests.get(url, headers=headers).text
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
for li in li_list:
    # 获取视频数字id
    video_id = li.xpath('./div/a/@href')[0].split('_')[-1]
    # 拼接视频url
    video_url = 'https://www.pearvideo.com/video_' + video_id
    # 获取视频标题
    video_title = li.xpath('./div/a/div[2]/text()')[0]
    # 拼接视频保存时的文件名
    video_file_title = video_title + '.mp4'
    # print(video_url, video_title)
    # 定义Ajax_url
    ajax_url = 'https://www.pearvideo.com/videoStatus.jsp'
    ajax_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'referer': video_url
    }
    pagram = {
        'contId': video_id,
        'mrd': str(random.random())
    }
    # 请求Ajax_url,获取json
    video_dirct = requests.get(ajax_url, headers=ajax_headers, params=pagram).json()
    # print(video_dirct)
    # 获取视频假链接
    video_fake_url = video_dirct.get('videoInfo', {}).get('videos', {}).get('srcUrl', '')
    system_time = video_dirct.get('systemTime', '')
    # 拼接视频真实链接
    video_real_url = re.sub(system_time, 'cont-' + video_id, video_fake_url)
    # 保存url到集合中
    real_urls = {
        'url': video_real_url,
        'name': video_file_title
    }
    urls.append(real_urls)

pool = Pool(4)
pool.map(download_video, urls)
