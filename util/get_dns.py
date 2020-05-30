# -*- coding: utf-8 -*-
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

    def write_host(self, filepath=''):
        pass


if __name__ == '__main__':

    parser = DNSParser('github.com')
    parser.print_result()    

    url = 'https://fastly.net.ipaddress.com/github.global.ssl.fastly.net'
    parser.print_result(url)
