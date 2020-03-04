# coding=gbk
import json
import os
import socket
import urllib.request
socket.setdefaulttimeout(10)
with open('log.txt', 'r') as f:
    n = int(f.read())
    print()
try:
    with open('hanman/manhua1.json', 'r') as f:
        mh_jsons = json.loads(f.read())
        for index, mh_json in enumerate(mh_jsons):
            path = f'manhua/{mh_jsons[n + index]["comic_name"]}/{mh_jsons[n + index]["comic_chapter_name"]}/'
            # if not os.path.isdir(path):
            print(f"{[n + index]}")
            try:
                os.makedirs(path)
            except:
                pass
            with open('log.txt', 'w+') as f:
                f.write(str(n + index))
            try:
                urllib.request.urlretrieve(mh_jsons[n + index]["img"], f'{path}/{mh_jsons[n + index]["i"]}.jpg')
            except:
                # 异常处理
                print("重启操作")
                # os.system("python download_img.py")
                with open('except.json', 'a+') as f:
                    f.write(f'{mh_jsons[n + index]}\n')
        with open('log.txt', 'w+') as f:
            f.write(str(0))
except socket.timeout:
    count = 1
    while count <= 5:
        urllib.request.urlretrieve(mh_jsons[n+index]["img"], f'{path}/{mh_jsons[n+index]["i"]}.jpg')
        break
    if count > 5:
        print("downloading picture fialed!")