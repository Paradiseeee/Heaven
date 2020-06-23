# -*- coding = utf-8 -*-

"""
Font:
    解决中文乱码、负号显示不正常
Animation：
    重写 matplotlib.animation.FuncAnimation 类的 save 方法，支持输出 GIF
"""
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os
import time
import imageio
import numpy as np

# Font
class Font:
    '''Setting font & axes'''

    def __init__(self):
        self.attrs = None
        print('\nCall self.setting() for quick setting-up\n')

    def set_font_family(self, font='Microsoft YaHei'):
        plt.rcParams['font.family'] = [font]

    def get_font_family(self):
        font_list = [f.name for f in mpl.font_manager.fontManager.ttflist]
        return sorted(font_list)

    def set_axis_unicode(self):
        plt.rcParams['axes.unicode_minus'] = False

    def setting(self, i=193):
        if i:
            self.set_font_family(self.get_font_family()[i])
        else:
            self.set_font_family()
        self.set_axis_unicode()


# Animation
class MyFuncAnimation(FuncAnimation):
    '''Overwrite *FuncAnimation.save* method'''

    def save(self, sample_rate=None, stop_index=None, index=None, quality=None, duration=0.3):
        
        print('\n> Generating, please wait ...\n')
        os.mkdir('./__TEMP__')
        frames = []
        
        # 如果 index 为空，根据采样率和终止序号，计算采样序号数组
        if not index:
            length = int((stop_index+1) * sample_rate)
            index = np.linspace(0, stop_index, length).astype(int)
        # 否则直接使用 index 传进来的数组
        else:
            pass
        
        for i in index:
            plt.close()
            self._func(i)
            # 如果 quality 为空，以正常质量保存
            if not quality:
                plt.savefig(f'./__TEMP__/{i}.jpg')
            # 否则进行图片压缩
            else:
                plt.savefig(f'./__TEMP__/{i}.jpg', quality=quality, 
                            optimize=True, papertype='letter', 
                            bbox_inches='tight', format='jpg')
            frames.append(imageio.imread(f'./__TEMP__/{i}.jpg'))
        
        imageio.mimsave('output.gif', frames, 'GIF', duration=duration)
        time.sleep(1)   # 等一会儿再删，不然会出现奇妙的现象
        os.system('rd/s/q __TEMP__')
        print('> Saved output.gif')
