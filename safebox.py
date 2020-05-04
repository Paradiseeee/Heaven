# coding = utf-8
"""
    生成一个藏文件的文件夹，通过指定6位密码指定文件夹，可以在公用电脑上使用。
"""

from os import mkdir
from time import time

if __name__ == "__main__":
    path = input('请输入安装路径：\n')
    # 创建密码字符集
    num = [i for i in range(10)]
    # 源目录
    mkdir(path + '/root')
    # 开始创建文件：
    start = time()
    for i in num:
        mkdir(path + f'/root/{i}')
    print(f'已完成第一层！\t共耗时{time() - start}秒')

    for i in num:
        for j in num:
            mkdir(path + f'/root/{i}/{j}')
    print(f'已完成第二层！\t共耗时{time() - start}秒')

    for i in num:
        for j in num:
            for k in num:
                mkdir(path + f'/root/{i}/{j}/{k}')
    print(f'已完成第三层！\t共耗时{time() - start}秒')

    for i in num:
        for j in num:
            for k in num:
                for x in num:
                    mkdir(path + f'/root/{i}/{j}/{k}/{x}')
    print(f'已完成第四层！\t共耗时{time() - start}秒')

    for i in num:
        for j in num:
            for k in num:
                for x in num:
                    for y in num:
                        mkdir(path + f'/root/{i}/{j}/{k}/{x}/{y}')
    print(f'已完成第五层！\t共耗时{time() - start}秒')

    for i in num:
        for j in num:
            for k in num:
                for x in num:
                    for y in num:
                        for z in num:
                            mkdir(path + f'/root/{i}/{j}/{k}/{x}/{y}/{z}')
    print(f'已完成第五层！\t共耗时{time() - start}秒')