# encoding=gbk
import os
import zipfile
path = os.path.abspath(os.curdir)
filenames = os.listdir()
for filename in filenames:
    if filename in ('.idea', 'showlist.py'):
        print(f"�ѹ���{filename}")
    else:
        path1 = f'{path}\\{filename}'
        try:
            filenames1 = os.listdir(path1)
        except:
            print("�Զ����˷�Ŀ¼�ļ�")
        zip = zipfile.ZipFile(f'{filename}.zip', 'w', zipfile.ZIP_DEFLATED)

        for filename1 in filenames1:
            path2 = f'{path1}\\{filename1}'
            fpath = os.path.join(path2, filename1)
            zip.write(path2, arcname=filename1)
            print(path2)
        zip.close()



