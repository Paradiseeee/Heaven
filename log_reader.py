# -*- coding: utf-8 -*-
"""
读取大型文本文件（1G以上）
"""

class LogReader():

    def __init__(self):
        self.filename = input('>>>请输入文件名（含路径）：\n')
        print('>>>正在读取，请稍后...\n')

    def get_lines(self):
        lines = 0
        for line in open(self.filename, 'r'):
            lines += 1
        print(f'\t 文件共 {lines} 行文本 \n')
    
    def get_slice(self):
        tpl = input('>>>请输入起始和结束行号，用逗号隔开：\n')
        tpl = tuple([t.strip() for t in tpl.split(',')])
        i = 1
        text = []
        for line in open(self.filename, 'r'):
            if i < tpl[0]:
                continue
            if i > tpl[1]:
                break
            text.append(line)
            i += 1
        with open(self.filename+'.slice.txt', 'w') as f:
            f.write(''.join(text))
        print(f'\t 已写出文件 {self.filename}.slice.txt')
    
    def print_slice(self):
        tpl = input('>>>请输入起始和结束行号，用逗号隔开：\n')
        tpl = tuple([t.strip() for t in tpl.split(',')])
        i = 1
        text = []
        for line in open(self.filename, 'r'):
            if i < tpl[0]:
                continue
            if i > tpl[1]:
                break
            print(line)
            i += 1

if __name__ == "__main__":

    lr = LogReader()
    while True:
        lr.print_slice()
        more = input('>>>是否继续读取？(y/n)\n')
        if more == 'n':
            break
