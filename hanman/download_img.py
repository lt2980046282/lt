# coding=gbk
import json
import os
import socket
import time
import urllib.request
from threading import Thread


class RunSpider(Thread):
    def __init__(self, page):
        self.page = page
        super(RunSpider, self).__init__()

    def run(self):
        manhua(self.page)


def manhua(page):
    socket.setdefaulttimeout(10)
    if not os.path.isfile(f'log{page}.txt'):
        with open(f'log{page}.txt', 'w+') as f:
            f.write('0')
            n = 0
            f.close()
    else:
        with open(f'log{page}.txt', 'r') as f:
            n = int(f.read())
            f.close()
    try:
        with open(f'hanman/manhua{page}.json', 'r') as f:
            mh_jsons = json.loads(f.read())
            for index, mh_json in enumerate(mh_jsons):
                path = f'manhua/{mh_jsons[n + index]["comic_name"]}/{mh_jsons[n + index]["comic_chapter_name"]}/'
                file_name = f'{path}/{mh_jsons[n + index]["i"]}.jpg'
                if not os.path.isfile(file_name):
                    print(f"{[n + index]}")
                    try:
                        os.makedirs(path)
                    except:
                        pass
                    try:
                        urllib.request.urlretrieve(mh_jsons[n + index]["img"], file_name)
                    except:
                        # 异常处理
                        print("重启操作")
                        RunSpider(page)
                        with open('except.json', 'a+') as f:
                            f.write(f'{mh_jsons[n + index]}\n')
                            f.close()
                    with open(f'log{page}.txt', 'w+') as f:
                        f.write(str(n + index))
                        f.close()
                else:
                    continue
    except socket.timeout:
        count = 1
        while count <= 5:
            urllib.request.urlretrieve(mh_jsons[n + index]["img"], f'{path}/{mh_jsons[n + index]["i"]}.jpg')
            break
        if count > 5:
            print("downloading picture fialed!")


def main():
    for index in range(1, 33):
        time.sleep(1)
        t = RunSpider(index)
        t.start()


if __name__ == '__main__':
    main()