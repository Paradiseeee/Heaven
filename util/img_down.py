# -*- coding: utf-8 -*-
"""Image DownLoader | Created to auto catch bing wallpaper"""
import os
import re
import time
import datetime
import requests as rq
from bs4 import BeautifulSoup


class DownLoader():
    '''[to-be-finished] download image from url'''
    
    def __init__(self):
        '''def params for downloader'''
        self.attrs = None
    
    def get(self, url, file):
        '''download from image-url'''

        print(f'\nDownloading {url}\n')
        res = rq.get(url, stream=True)
        with open(file, 'wb') as f:
            f.write(res.content)


def get_bing_bg():
    '''get url of bing-home-page background'''

    host = 'https://cn.bing.com'
    res = rq.get(host)
    url = re.compile('(th\?id=.*?\.jpg)').findall(res.text)[0].split('_')
    _ = url.pop()
    url = '/' + '_'.join(url)

    return host + url


if __name__ == "__main__":

    url = get_bing_bg()
    date_str = str(datetime.date.today())
    file = f"C:/Users/Paradise/Pictures/BING/{date_str}.{url.split('.')[-1]}"
    DownLoader().get(url, file)
    size = os.path.getsize(file)/1024/1024
    # useless sh*t
    for i in range(75):
        text = '=' * i
        print('\r %s' % text, end='》')
        time.sleep(0.01)
    print(f'\n\nImage saved to {file} ({round(size, 2)} MB)\n')
    time.sleep(1)
