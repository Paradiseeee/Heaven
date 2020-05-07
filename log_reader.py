# -*- coding: utf-8 -*-
"""
读取大型文本文件（1G以上）
"""

class LogReader():

    def __init__(self):
        self.encode = 'utf-8'
        self.filename = input('>>>请输入文件名（含路径）：\n')
        print('>>>正在读取，请稍后...\n')

    def get_lines(self):
        lines = 0
        for line in open(self.filename, 'r', encoding=self.encode):
            lines += 1
        print(f'\t 文件共 {lines} 行文本 \n')
    
    def get_slice(self, encoding='utf-8'):
        tpl = input('>>>请输入起始和结束行号，用逗号隔开：\n')
        tpl = tuple([int(t.strip()) for t in tpl.split(',')])
        i = 1
        text = []
        for line in open(self.filename, 'r', encoding=self.encode):
            if i < tpl[0]:
                continue
            if i > tpl[1]:
                break
            text.append(line)
            i += 1
        with open(self.filename+'.slice.txt', 'w', encoding=self.encode) as f:
            f.write(''.join(text))
        print(f'\t 已写出文件 {self.filename}.slice.txt')
    
    def print_slice(self, encoding='utf-8'):
        tpl = input('>>>请输入起始和结束行号，用逗号隔开：\n')
        tpl = tuple([int(t.strip()) for t in tpl.split(',')])
        i = 1
        text = []
        for line in open(self.filename, 'r', encoding=self.encode):
            if i < tpl[0]:
                continue
            if i > tpl[1]:
                break
            print(line)
            i += 1

if __name__ == "__main__":

    lr = LogReader()
    try:
        lr.get_lines()
    except:
        lr.encode = 'gbk'
        lr.get_lines()
    while True:
        try:
            lr.print_slice()
        except:
            print('\t 行号错误！')
        more = input('>>>是否继续读取？(y/n)\n')
        if more == 'n':
            break
