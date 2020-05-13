# -*- coding: utf-8 -*-
"""
用于记一些隐私的文本笔记，windows 自带的 sticker 和 Office 不好用，还是
用命令行香。
"""
import os
from Heaven import __ROOT__

try:
    os.mkdir(__ROOT__ + '\\DOCUMENTS')
except:
    os.chdir(__ROOT__ + '\\DOCUMNETS')

def update_pointer():
    pass

def readnote():
    pass

def writenote():
    pass

def get_doc_num():
    pass

def clear_all():
    pass

if __name__ == "__main__":

    rw = input('\n>>> 选择任务：读取（1）| 写入（2）\n')

    if rw == '1':
        with open('__POINTER__', 'r', encoding='utf-8') as f:
            pointer = f.read()
            print(f'{pointer}.pynote'.center(72, '_'))
        
        
    
    elif rw == '2':
        new = input('\n>>> 命名新笔记：\n')
        with open('__POINTER__', 'w') as f:
            f.write(new + '.pynote')

        print('\n>>> 输入内容，输入（q）退出\n')
        while True:
            with open(f'{new}.pynote', 'a') as f:
                line = input(':')
                if line == 'q':
                    print(f'\n>>> 成功写出文件 {new}.pynote\n')
                    break
                else:
                    f.write(line)
