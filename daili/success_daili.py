import os
import time
from threading import Thread
import requests
import dlmsql


class CheckSuccessProxy(Thread):
    global success_ip_list
    success_ip_list = []

    def __init__(self, ip):
        self.ip = ip
        super(CheckSuccessProxy, self).__init__()

    def run(self):
        check_ip(self.ip)


def read_iplist():
    ls = dlmsql.showList('successstore')
    if not ls is None:
        success_ip_list.extend(ls)


def del_ip(ip):
    return dlmsql.dlt('successstore', ip)


def ins_ip(ip):
    return dlmsql.add('failstore', ip)


# 检测IP是否可用
def check_ip(ip):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    proxies = {'http': f'http://{ip}', 'https': f'https://{ip}'}
    try:
        # 请求连接是否可以访问
        requests.get('https://www.baidu.com/s?wd=ip', headers=headers, proxies=proxies, timeout=3)
        print(f'IP池过滤:success-{ip}')
    except:
        print(f'IP池过滤:fail-{ip}')
        time.sleep(1)
        del_ip(ip)
        ins_ip(ip)


def main():
    threads = []
    if len(success_ip_list) > 0:
        for index, ip in enumerate(success_ip_list):
            time.sleep(1)
            t = CheckSuccessProxy(ip)
            threads.append(t)
            t.start()
        for t in enumerate(threads):
            try:
                t.join()
            except:
                break


# 程序入口 接入代理只要把获取的IP列表装入plist即可
# xxxxx()
# main()此为一个完整的接口
if __name__ == '__main__':
    while True:
        read_iplist()
        main()
