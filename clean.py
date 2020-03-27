import shutil
import os
from os import listdir
from os import walk
from os.path import isfile, join

path=[r"C:\Windows\Temp",r"C:\Users\lenovo\AppData\Local\Temp",r"C:\Windows\Prefetch"]


f=[]
d=[]
dir_path=[]

for l_path in path:
    
    for (dirpath, dirnames, filenames) in walk(l_path):
        print(filenames)
        f.extend(filenames)
        d.extend(dirnames)
        dir_path.append(dirpath)
        break

    print(f)
    print(d)
    print(dir_path)


    for p in d:
        if isfile(join(l_path,p)):
            try:
                os.remove(join(l_path,p))
            except:
                pass
        else:
            try:
                shutil.rmtree(join(l_path,p), ignore_errors=False)
            except:
                pass

    for p in f:
        if isfile(join(l_path,p)):
            try:
                os.remove(join(l_path,p))
            except:
                pass
        else:
            try:
                shutil.rmtree(join(l_path,p), ignore_errors=False)
            except:
                pass




    
        




