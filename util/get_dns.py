# -*- coding: utf-8 -*-
import os
import time
import pyautogui as pag
from pandas import read_html


class DNSParser():
    '''自动获取域名的dns并修改host文件'''

    def __init__(self, domain):
        '''Initializing'''
        self.domain = domain
        self.url = f'https://{domain}.ipaddress.com'
    
    def parse_result(self):
        dfs = read_html(self.url)
        return dfs[0]

    def print_result(self, url=None):
        '''打印结果，同时允许通过URL参数更改对象的url和domain属性'''
        if url:
            self.url = url
            self.domain = url.split('/')[-1]
        print(f'\n>>> {self.domain}\n' + '-'*80)
        df = self.parse_result()
        print(df.to_markdown())

        return df

    def write_host(self, domain):
        '''不可移植使用'''
        # 打开 geany
        pag.press('win'); pag.write('geany'); time.sleep(1); pag.press('enter')
        pag.hotkey('ctrl', 'shift'); pag.hotkey('ctrl', 'shift')
        # 打开notepad
        pag.hotkey('win', 'r');time.sleep(0.2)
        pag.write('notepad C:\Windows\System32\drivers\etc\hosts');pag.press('enter')
        pag.hotkey('ctrl', 'shift');pag.hotkey('ctrl', 'shift')
        # 定位、修改、保存
        pag.moveTo(1500, 1000, 0.2); pag.click(); 
        pag.hotkey('shift', 'up'); pag.press('backspace'); 
        pag.write(domain+' '); pag.write('github.com\n'); 
        pag.hotkey('ctrl', 's'); time.sleep(0.5); pag.hotkey('alt', 'f4')
        # 刷新
        for _ in range(5):
            os.system('ipconfig /flushdns')


if __name__ == '__main__':

    parser = DNSParser('github.com')
    df = parser.print_result()
    ipv4 = dict(zip(df[0], df[1]))['IP Address']
    
    url = 'https://fastly.net.ipaddress.com/github.global.ssl.fastly.net'
    parser.print_result(url)
    parser.write_host(ipv4)
