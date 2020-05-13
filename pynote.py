# -*- coding: utf-8 -*-
"""
用于记一些隐私的文本笔记，windows 自带的 sticker 和 Office 不好用，还是
用命令行香。
"""
import os
from Heaven import __ROOT__

class PyNote():

    def __init__(self):
        '''Initializing'''
        try:
            os.mkdir(__ROOT__ + '\\DOCUMENTS')
        except:
            os.chdir(__ROOT__ + '\\DOCUMENTS')
        self.mode = input('\n>>> 选择任务：读取（1）| 写入（2）\n')
        self.new = None

    def update_pointer(self):
        self.new = input('\n>>> 命名新笔记：\n')
        with open('__POINTER__', 'w') as f:
            f.write(self.new + '.pynote')
    
    def writenote(self):
        print('\n>>> 输入内容，输入（q）退出\n')
        while True:
            with open(f'{self.new}.pynote', 'a') as f:
                line = input(':')
                if line == 'q':
                    print(f'\n>>> 成功写出文件 {self.new}.pynote\n')
                    break
                else:
                    f.write(line + '\n')

    def readnote(self):
        try:
            with open('__POINTER__', 'r', encoding='utf-8') as f:
                pointer = f.read()
            print(pointer.center(72, '_'))
            with open(pointer, 'r', encoding='utf-8') as f:
                print(f.read())
        except:
            print('暂无笔记，请添加笔记！')

    def get_doc_num():
        pass

    def clear_all():
        pass


if __name__ == "__main__":

    noter = PyNote()
    if noter.mode == '1':
        noter.readnote()
    elif noter.mode == '2':
        noter.update_pointer()
        noter.writenote()