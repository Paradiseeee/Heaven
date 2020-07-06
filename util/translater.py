# -*- coding: utf-8 -*-
import re
import json
import win32clipboard as wc
from win32con import CF_TEXT

# http://api.fanyi.baidu.com/doc/21

def getclipboard():

    wc.OpenClipboard()
    text = wc.GetClipboardData(CF_TEXT)
    wc.CloseClipboard()
    try:
        return text.decode()
    except:
        return text.decode('gbk')

def remove_esc(text):

    for t in ['\r', '\n', '\t']:
        text = text.replace(t, ' ')
    return text


if __name__ == "__main__":

    print(remove_esc(getclipboard()))
