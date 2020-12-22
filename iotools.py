# -*- coding: utf-8 -*-
"""System Programming helper
"""

import os
import shutil
import numpy as np
import pandas as pd

def iterfiles(root, depth, *suffix):
    '''Return all files' path in root, with given suffix'''
    
    gen = os.walk(root)
    itemlist = list(gen)
    output = []
    for item in itemlist:
        filelist = [item[0]+'/'+f for f in item[2]]
        for f in filelist:
            if f.split('.')[-1] in suffix or not suffix:
                output.append(f.replace('\\', '/'))
    output = pd.Series(output)
    index = output.str.split('/').map(lambda x: len(x)<=depth)

    return list(output.loc[index])


if __name__ == "__main__":

    help(iterfiles)
