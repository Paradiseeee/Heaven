# -*- coding: utf-8 -*-
"""
DataScience Toolkits
"""

import os
import sys

from .mysql_helper import MysqlHelper
from .pdf_processor import PDFProcessor
from .log_reader import LogReader
from .get_dns import DNSParser
from .make_ico import ICOGenerator

# Module Attributes
__doc__ = '''
I am trying to build a module for specific field of data science, and
at the same time learn to manage a public project.

It just started, and I will put anything I like in here, which doesn't 
have to be related with data science, just to enhance my workflow.

If everything goes well, I will make it more specific and usefull in 
the next version. I am new to this whole thing and I look forward some 
usefull advices.

If anyone is interested to this, please let me know:
 <paradise26472@qq.com;>
 <paradise-yang@outlook.com;>

More Information About This Module:
 <https://github.com/paradiseeee/Heaven>

My GitHub Page:
 <https://paradiseeee.github.io>'''
__author__ = "Paradise (github.com/paradiseeee)"
__version__ = "1.0"
__copyright__ = "Copyright (c) 2019-2020 Paradise"
__license__ = "MIT"

# User Attributes
__ROOT__ = sys.executable.replace('python.exe', 'lib\\Heaven')


def get_license():
    with open('LICENSE', 'r') as f:
        text = f.read()
    print(text)


def get_modules(path=__ROOT__, suffix='py'):
    os.chdir(path)
    files = [i.split('.') for i in sorted(os.listdir())]
    max_length = max([len(f) for f in os.listdir()])
    for f in files:
        if len(f) == 1 and f[0] not in ['__pycache__', 'LICENSE']:
            text = f[0].rjust(max_length-1) + '/' + ' | [P]Path'
            print(text.center(80-max_length, ' '))
    for f in files:
        if suffix in f:
            text = '.'.join(f).rjust(max_length) + ' | [F]File'
            print(text.center(80-max_length, ' '))


if __name__ == "__main__":

    print('\n' + ' Welcome to Heaven! '.center(72, '_'))
    print(__doc__)

    print('\n' + ' Module List '.center(72, '_') + '\n')
    get_modules()
