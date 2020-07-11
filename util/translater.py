﻿# -*- coding: utf-8 -*-
"""
REFER | <http://api.fanyi.baidu.com/doc>
"""
import re
import json
import random
import hashlib
import requests as rq
import win32clipboard as wc
from win32con import CF_TEXT
from Heaven import __ROOT__


class Translater():
    '''调用百度API英汉互译'''

    def __init__(self, mode='cmd'):
        '''initialization'''

        self.MODE = mode
        with open(__ROOT__+'/_UserKeys/baidu-trans-key.json', 'r') as f:
            self.API = json.loads(f.read())
        self.URL = self.generate_url()

    def generate_url(self):
        '''生成请求链接'''

        # 全为英文时使用英译中，否则中译英
        query = self.getclipboard()
        bool_map = map(lambda s: '\u4e00'<=s<='\u9fa5', query)
        lang = ('en', 'zh') if sum(bool_map) == 0 else ('zh', 'en')
        salt = str(random.randint(32768, 65536))
        sign = self.API['API_ID'] + query + salt + self.API['API_KEY']
        sign = hashlib.md5(sign.encode()).hexdigest()

        url = 'http://api.fanyi.baidu.com/api/trans/vip/translate?'
        url += f'q={query}&from={lang[0]}&to={lang[1]}'
        url += f'&appid={self.API['API_ID']}&salt={salt}&sign={sign}'

        return url

    def getclipboard(self):

        wc.OpenClipboard()
        text = wc.GetClipboardData(CF_TEXT)
        wc.CloseClipboard()
        try:
            text = text.decode()
        except:
            text = text.decode('gbk')
        for t in ['\r', '\n', '\t']:
            text = text.replace(t, ' ')
        
        return text


if __name__ == "__main__":

    print(Translater().getclipboard())
