# -*- coding: utf-8 -*-
import json
import random
import urllib
import hashlib
import http.client
import win32clipboard
import tkinter as tk
from win32con import CF_TEXT

class Translater:
    def __init__(self):
        self.API = {'API_ID': '******', 'API_KEY': '******'}
        self.PrevCopyed = None
    def translate(self):
        myurl = self.generate_url()
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            results = json.loads(result_all)['trans_result']
            ret = '\n'.join([r['dst'] for r in results])
        except Exception as e:
            ret = 'Something wring during translating: ' + str(e)
        finally:
            if httpClient:
                httpClient.close()
        return ret

    def generate_url(self):
        query = self.getclipboard()
        bool_map = map(lambda s: '\u4e00'<=s<='\u9fa5', query)
        lang = ('en', 'zh') if sum(bool_map) == 0 else ('zh', 'en')
        salt = str(random.randint(32768, 65536))
        sign = self.API['API_ID'] + query + salt + self.API['API_KEY']
        sign = hashlib.md5(sign.encode()).hexdigest()
        url = 'http://api.fanyi.baidu.com/api/trans/vip/translate?'
        url += f'q={urllib.parse.quote(query)}&from={lang[0]}&to={lang[1]}'
        url += f"&appid={self.API['API_ID']}&salt={salt}&sign={sign}"
        return url

    def getclipboard(self):
        win32clipboard.OpenClipboard()
        try:
            text = win32clipboard.GetClipboardData(CF_TEXT)
        except:
            text = 'Invalid Clipboard Format'.encode()
        win32clipboard.CloseClipboard()
        try:
            text = text.decode()
        except:
            text = text.decode('gbk')
        return text

    def window(self):
        root = tk.Tk()
        root.geometry("+0+0")
        root.configure(bg='#000000')
        root.overrideredirect(True)
        root.wm_attributes('-alpha', 0.77)
        root.wm_attributes('-topmost', True)
        var = tk.StringVar()
        label = tk.Label(root, textvariable=var, fg='#ffffff', bg='#000000', relief='sunken')
        def get_result():
            if not self.PrevCopyed:
                var.set(' Welcome to the Most Wonderful Translater in the Whole F**king World ! ')
                label.pack()
                self.PrevCopyed = self.getclipboard()
            if self.getclipboard() != self.PrevCopyed:
                try:
                    text = '\u27A4   ' + self.translate()
                except Exception as e:
                    text = f'ERROR: {str(e)}'
                var.set(text)
                label.pack()
                self.PrevCopyed = self.getclipboard()
            root.after(100, get_result)
        root.after(0, get_result)
        root.mainloop()

if __name__ == "__main__":

    Translater().window()
