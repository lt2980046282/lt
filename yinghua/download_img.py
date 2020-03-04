# encoding=gbk
import json
import os
import urllib
import requests
with open('log.txt', 'r+') as f:
    n = int(f.read())
    print()
    with open('yinghua3.json', 'r') as f:
        yh_jsons = json.loads(f.read())
        for index, yh_json in enumerate(yh_jsons):
            sum = index +n
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
            with open('log.txt', 'w') as fa:
                fa.write(str(sum))
                content = requests.get(yh_jsons[sum]['url']).content
            with open(f'{path}/{yh_jsons[sum]["i"]}.jpg', 'wb') as fs:
                fs.write(content)


                # urllib.request.urlretrieve(yh_jsons[n + index]["url"], f'{path}/{yh_jsons[n + index]["i"]}.jpg')
            # except:
            #     # 异常处理
            #     print("重启操作")
            #     # os.system("python download_img.py")
            #     with open('except.json', 'a+') as f:
            #         f.write(f'{yh_jsons[n + index]}\n')


