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

    def write_host(self, filepath=''):
        pass


if __name__ == '__main__':

    parser = DNSParser('github.com')
    print('\n>>> github.com\n' + '-'*80)
    print(parser.parse_result().to_markdown())

    print('\n>>> github.global.ssl.fastly.net\n' + '-'*80)
    parser.url = 'https://fastly.net.ipaddress.com/github.global.ssl.fastly.net'
    print(parser.parse_result().to_markdown())
