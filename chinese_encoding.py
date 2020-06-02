# -*- coding = utf-8 -*-

"""
每次用 matplotlib 绘图都要解决一下中文乱码问题，这几段代码又难记，打包起来
绘图前：from Heaven.chinese_encoding import *
"""
import matplotlib as mpl
import matplotlib.pyplot as plt


def set_font_family(font):
    plt.rcParams['font.family'] = [font]

def get_font_family():
    font_list = [f.name for f in mpl.font_manager.fontManager.ttflist]
    return sorted(font_list)

plt.rcParams['axes.unicode_minus'] = False
set_font_family('Microsoft YaHei')