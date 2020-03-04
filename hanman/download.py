# coding=gbk
import json
import os
import socket
import urllib.request

n = 0
#设置超时时间为5s
socket.setdefaulttimeout(10)
#解决下载不完全问题且避免陷入死循环


def auto_download(n):
    with open('hanman/manhua31.json', 'r') as f:
        mh_jsons = json.loads(f.read())
        for index, mh_json in enumerate(mh_jsons):
            path = f'manhua/{mh_jsons[n + index]["comic_name"]}/{mh_jsons[n + index]["comic_chapter_name"]}/'
            i = index
            print(f"{[n + index]}")
            try:
                os.makedirs(path)
            except:
                print("处理异常")
            try:
                urllib.request.urlretrieve(mh_jsons[n + index]["img"], f'{path}/{mh_jsons[n + index]["i"]}.jpg')
            except:
                os.system("python download_img.py")
            return n + index
try:
    n = auto_download(n)
    print(n)
except socket.timeout:
    count = 1
    while count <= 5:
        try:
            n = auto_download(n)
            break
        except socket.timeout:
            err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
            print(err_info)
            count += 1
    if count > 5:
        print("downloading picture fialed!")

