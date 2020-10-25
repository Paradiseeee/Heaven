# -*- coding: utf-8 -*-
"""
REFER | <http://api.fanyi.baidu.com/doc>
平时经常阅读英文文档，浏览器有翻译插件，但是其他软件中翻译就比较麻烦；
使用第三方的辞典软件翻译结果不理想，并且平时一般只需要翻译某一个单词或者长难句；
而第三方软件的划词和取词功能也不符合阅读习惯，用户体验极差；
因此 DIY 一个符合自己需求的便捷的全局翻译“插件”。
只需要复制需要翻译的文本，自动中英互译。如果需要翻译特定内容，只需在任意位置输入然后复制。
"""
import json
import random
import urllib
import hashlib
import http.client
import win32clipboard
import tkinter as tk
from win32con import CF_TEXT
from Heaven import __ROOT__


class Translater():
    '''调用百度API英汉互译'''

    def __init__(self, fromClipboard='True'):
        '''initialization'''

        self.PrevCopyed = None
        self.fromClipboard = fromClipboard
        with open(__ROOT__+'/_UserKeys/baidu-trans-key.json', 'r') as f:
            self.API = json.loads(f.read())


    def translate(self, text='if fromClipboard=True, ignore this text'):
        '''main function'''

        try:
            if self.fromClipboard:
                query = self.getclipboard()
            else:
                query = text
            myurl = self.generate_url(query)
        except Exception as e:
            # return
            ret = 'Something wrong during generating URL: ' + str(e)

        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            results = json.loads(result_all)['trans_result']
            # return
            ret = '\n'.join([r['dst'] for r in results])

        except Exception as e:
            # return
            ret = 'Something wring during translating: ' + str(e)
        
        finally:
            # 需要关闭连接，不能在上面直接返回值
            if httpClient:
                httpClient.close()

        return ret


    def generate_url(self, query):
        '''generate API URL'''

        # 全为英文时使用英译中，否则中译英
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
        '''get text from clipboard; used when self.fromClipboard=True(default)'''

        win32clipboard.OpenClipboard()
        try:
            text = win32clipboard.GetClipboardData(CF_TEXT)
        except:
            text = 'Invalid Clipboard Format'.encode()
        win32clipboard.CloseClipboard()     # 打开后必须手动关闭

        try:
            text = text.decode()
        except:
            text = text.decode('gbk')
        
        return text


    def window(self):
        '''desktop window powered by tkinter'''

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
