# coding=gbk
import json
import os
import socket
import urllib.request

socket.setdefaulttimeout(30)
with open('log.txt', 'r+') as f:
    n = int(f.read())
    print()
try:
    with open('yinghua1.json', 'r') as f:
        yh_jsons = json.loads(f.read())
        for index, yh_json in enumerate(yh_jsons):
            sum = index + n
            name = yh_jsons[sum]["name"]
            name = str(name).replace('\n', '')
            name = name.replace('/', '')
            path = f'yinghua/{name}/'
            # if not os.path.isdir(path):
            print(f"{[sum]}")
            try:
                os.makedirs(path)
            except:
                pass
            with open('log.txt', 'w+') as f:
                f.write(str(sum))
            # try:
                urllib.request.urlretrieve(yh_jsons[sum]["url"], f'{path}/{yh_jsons[sum]["i"]}.jpg')
            # except:
            #     # 异常处理
            #     print("重启操作")
            #     # os.system("python download_img.py")
            #     with open('except.json', 'a+') as f:
            #         f.write(f'{yh_jsons[sum]}\n')
        with open('log.txt', 'w+') as f:
            f.write(str(0))
except socket.timeout:
    count = 1
    while count <= 5:
        urllib.request.urlretrieve(yh_jsons[n + index]["url"], f'{path}/{yh_jsons[n + index]["i"]}.jpg')
        break
    if count > 5:
        print("downloading picture fialed!")
