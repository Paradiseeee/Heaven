# coding = utf-8

"""
    当绘图中有中文出现乱码，执行--
    from my_module.chinese_coding import *
"""

import matplotlib.pyplot as plt

# 解决中文乱码问题
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号