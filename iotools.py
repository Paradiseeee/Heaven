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

def walkdir(top):
    '''Return a list of all folders and a list of files'''

    gen = os.walk(top)
    files = []
    folders = []
    for root, folder, file in gen:
        for f in file:
            files.append(root + '/' + f)
        for d in folder:
            folders.append(root + '/' + d)
    files = [f.replace('\\', '/').replace('//', '/') for f in files]
    folders = [d.replace('\\', '/').replace('//', '/') for d in folders]
    
    return files, folders


if __name__ == "__main__":

    help(iterfiles)
