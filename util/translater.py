# -*- coding: utf-8 -*-
"""
REFER | <http://api.fanyi.baidu.com/doc>
"""
import re
import json
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
            self.KEYS = json.loads(f.read())

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
