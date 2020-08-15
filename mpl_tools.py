# -*- coding = utf-8 -*-
""" Frequently Used Functions for Matplotlib
"""
import os
import time
import imageio
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


class Begin:
    '''Setting font, style & axes'''

    def __init__(self):
        self.attrs = None
        print('\nCall self.get_font_family to get available fonts')
        print('\nCall self.get_style to get available styles')

    def get_font_family(self):
        font_list = [f.name for f in mpl.font_manager.fontManager.ttflist]
        return sorted(font_list)

    def set_font_family(self, font='Microsoft YaHei'):
        plt.rcParams['font.family'] = [font]

    def get_style(self):
        return plt.style.available

    def set_style(self, style='dark_background'):
        plt.style.use(style)

    def set_axis_unicode(self):
        plt.rcParams['axes.unicode_minus'] = False

    def setting(self, **kwargs):
        '''This is for quickly setup'''
        self.set_axis_unicode()
        self.set_font_family()
        self.set_style()


class MyFuncAnimation(FuncAnimation):
    '''Overwrite *FuncAnimation.save* method to save GIF'''

    def save(self, sample_rate=None, stop_index=None, index=None, quality=None, duration=0.2):
        
        print('\n> Generating, please wait ...\n')
        os.mkdir('./__TEMP__')
        frames = []

        if not index:
            length = int((stop_index+1) * sample_rate)
            index = np.linspace(0, stop_index, length).astype(int)

        for i in index:
            plt.close()
            self._func(i)
            if not quality:
                plt.savefig(f'./__TEMP__/{i}.jpg')
            else:
                plt.savefig(f'./__TEMP__/{i}.jpg', 
                    quality=quality, optimize=True, 
                    papertype='letter', bbox_inches='tight', format='jpg'
                    )
            frames.append(imageio.imread(f'./__TEMP__/{i}.jpg'))
        
        imageio.mimsave('output.gif', frames, 'GIF', duration=duration)
        time.sleep(1)
        os.system('rd/s/q __TEMP__')
        print('> Saved output.gif')


if __name__ == "__main__":

    examples = '''
    Begin().setting()
    ani = MyFuncAnimation(fig, func, interval=100)
    ani.save()
    '''
    print(examples)
