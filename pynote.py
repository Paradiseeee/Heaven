# -*- coding: utf-8 -*-
"""
用于记一些隐私的文本笔记，windows 自带的 sticker 和 Office 不好用，还是
用命令行香。
"""
import os
import shutil
from Heaven import __ROOT__, get_modules

class PyNote():

    def __init__(self):
        '''Initializing'''
        self.mode = input('\n>>> 选择任务：读取（1）| 写入（2）| 清空（3）\n')
        self.docpath = __ROOT__ + '\\DOCUMENTS'
        self.new = None

    def writenote(self):
        self.new = input('\n>>> 命名新笔记：\n')
        with open('__POINTER__', 'w') as f:
            f.write(self.new + '.pynote')
        print('\n>>> 输入内容，输入（q）退出\n')
        while True:
            with open(f'{self.new}.pynote', 'a', encoding='utf-8') as f:
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

    def clear_all(self):
        print('>>> 删除以下文件：')
        try:
            get_modules(self.docpath, suffix='pynote', '__POINTER__')
        except:
            print('暂无笔记，请添加笔记！')
            return 0
        confirm = input('>>> 是否继续？（y/n）')
        if confirm == 'y':
            try:
                shutil.rmtree(self.docpath)
            except Exception as e:
                print(e)

    def main(self):
        try:
            os.mkdir(self.docpath)
            os.chdir(self.docpath)
        except:
            os.chdir(self.docpath)
        if self.mode == '1':
            self.readnote()
        elif self.mode == '2':
            self.writenote()
        elif self.mode == '3':
            self.clear_all()

if __name__ == '__main__':

    PyNote().main()