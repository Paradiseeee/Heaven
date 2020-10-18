# -*- coding: utf-8 -*-
""" Spider Helper - Frequently Used Functions in Spider-Development
"""
import re
import http
import wget
import urllib
import requests as rq
from bs4 import BeautifulSoup

WINDOWS_UA = 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
LINUX_UA = 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36'


def get_cookies(url):
    '''Return cookies dict of url'''

    jar = http.cookiejar.CookieJar()
    processor = urllib.request.HTTPCookieProcessor(jar)
    opener = urllib.request.build_opener(processor)

    _ = opener.open(url)
    cookies = []
    for i in jar:
        cookies.append(i.name + '=' + i.value)

    return {'Cookie': '; '.join(cookies)}


def get_response(url, user_agent=WINDOWS_UA, show=False, save=False, **headers):
    ''' Return response of GET requets
    PARAMETERS:
           url  | get
    user_agent  | different from pc and mobile
          show  | Quick view of web page
          save  | Save to output.html
     **headers  | other header parameters
    '''

    headers.update({'User-Agent': user_agent})
    res = rq.get(url, headers=headers)

    if show:
        text = re.compile('>([^\x00-\xff]+)<').findall(res.text)
        print(' | '.join(text))
    elif save:
        with open('output.html', 'w', encoding='utf-8') as f:
            f.write(res.text)
    else:
        print(res.status_code)
        return res


def batchdown(url, tag='img', attr='data-src', suffix='png'):
    '''
    Download all attr-link in specific tag, and save with suffix;
    Default download img and save as png.
    '''
    res = get_response(url)
    soup = BeautifulSoup(res.text, features='lxml')
    links = soup.find_all(tag)
    i = 0
    print('\nStart Downloading ...')
    for link in links:
        try:
            wget.download(link.attrs[attr], out=f'{i}.{suffix}')
            i += 1
        except:
            continue
    print('\nFinish Downloading !')


if __name__ == "__main__":

    examples = '''
    url = 'https://www.baidu.com'
    cookies = get_cookies(url)
    res1 = get_response(url, show=True, Cookie=cookies['Cookie'])
    res2 = get_response(url, save=True, **cookies)
    '''
    print(examples)

