# coding = utf-8
"""
    show orthers I am a hacker!
    暂时已经完结，不打算添加新的功能。
"""
import time
from numpy import random

text = "1234567890qwertyuiopasdfghjklzxcvbnm~`!@#$%^&*()_-+={}[]|\\:;'\"<>,./?"
text_list = list(text)
text_list += list(" "*22)
text_list += list("\n"*5)
text_list += list("\t"*5)

def get_index80(_range_):
    index = []
    while len(index) <= 75:
        idx = random.randint(_range_)
        if idx not in index:
            index.append(idx)
    return index

def byteflow(n):
    text_list = list("__||"*100)
    for i in range(n):
        index = get_index80(len(text_list))
        text = ""
        for t in [text_list[idx] for idx in index]:
            text += t
        print(text)

def byteflow2(n):
    text_list = list("0011"*100)
    for i in range(n):
        index = get_index80(len(text_list))
        text = ""
        for t in [text_list[idx] for idx in index]:
            text += t
        print(text)

def showoff(n):
    for i in range(n):
        index = get_index80(len(text_list))
        text = ""
        for t in [text_list[idx] for idx in index]:
            text += t
        print(text)

def bullbeer():
    text = """
                    +-------------------------------------------+
                    |                                           |
                    |               Successfull！               |
                    |         成功控制美国五角大楼服务器！      |
                    |                                           |
                    +-------------------------------------------+
    已启动加强防守模式，连接维持中。。。
    。。。
    请输入脚本执行任意读写操作：
    """
    print(text)

def trick():
    time.sleep(5)
    print("为防止反侵入，连接将于10秒后中断。。。")
    t = 10
    for i in range(10):
        time.sleep(1)
        print(t)
        t = t - 1

def main():
    byteflow(5000)
    byteflow2(5000)
    showoff(5000)
    bullbeer()

if __name__ == '__main__':
    main()