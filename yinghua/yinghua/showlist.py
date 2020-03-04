import os
import zipfile
path = os.path.abspath(os.curdir)
filenames = os.listdir()
for filename in filenames:
    path1 = f'{path}/{filename}'
    filenames1 = os.listdir(path1)
    print(filenames1)
