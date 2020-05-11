# -*- coding: utf-8 -*-
"""
DataScience Toolkits
"""

__doc__ = '''
I am trying to build a module for specific field of data science.
At the same time learn to manage a public project.

It just started, and I will put anything I like in here, which doesn't 
have to be related with data science, just to enhance my workflow.

If everything goes well, I will make it more specific and usefull in 
the next version.I am new to this whole thing and I look forward some 
usefull advices.

If anyone is interested to this, please let me know:
paradise26472@qq.com;
paradise-yang@outlook.com; 

More Information About This Module:
https://github.com/paradiseeee/Heaven

My GitHub Page:
https://paradiseeee.github.io'''

__author__ = "Paradise (github.com/paradiseeee)"
__version__ = "1.0"
__copyright__ = "Copyright (c) 2019-2020 Paradise"
# Use of this source code is governed by the MIT license.
__license__ = "MIT"

import os

from .mysql_helper import MysqlHelper
from .pdf_processor import PDFProcessor
from .log_reader import LogReader
from .get_dns import DNSParser


def get_license():
    with open('LICENSE', 'r') as f:
        text = f.read()
    print(text)

def get_modules():
    files = [i.split('.') for i in sorted(os.listdir())]
    for f in files:
        if 'py' in f:
            print('\t' + '.'.join(f))
    for f in files:
        if len(f) == 1 and f[0] not in ['__pycache__', 'LICENSE']:
            print(f[0] + '/')


if __name__ == "__main__":
    
    print(' Welcome to Heaven! '.center(72, '_'))
    print(__doc__)

    print(' Module List '.center(72, '_'))
    get_modules
