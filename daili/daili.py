import os
import time
from threading import Thread, Lock

import requests
from lxml import etree
from urllib3.exceptions import MaxRetryError
from setting import config
import dlmysql


class Proxies(Thread):
    global plist
    #
    plist = []
    # # 判断文本中是存在测试成功的ip
    # success_success_ip_list = dlmsql.showList('successstore')
    # if len(success_success_ip_list) > 0:
    #     success_ip_list = success_success_ip_list
    # fail_ip_list = []
    # # 判断文本中是存在测试失败的ip
    # temp_fail_ip_list = dlmsql.showList('failstore')
    # if len(temp_fail_ip_list) > 0:
    #     fail_ip_list = temp_fail_ip_list
    # # # 全局ip列表
    ip = ''

    def __init__(self, ip):
        self.ip = ip
        super(Proxies, self).__init__()

    def run(self):
        check_ip(self.ip)


def getIplist():
    response = requests.get('http://www.89ip.cn/tqdl.html?api=1&num=9999')
    response.encoding = 'utf-8'
    html = response.content
    tree = etree.HTML(html)
    ip_list = tree.xpath('//body/text()')
    del ip_list[0]
    del ip_list[0]
    ip_list.pop()
    ip_list[0] = ip_list[0].replace('\n', '')
    plist.extend(ip_list)


def getKDLIpList():
    for page in range(50):
        try:
            response = requests.get(url=f'https://www.kuaidaili.com/free/intr/{page}')
        except:
            os.system('py daili.py')
        time.sleep(1)
        response.encoding = 'utf-8'
        html = response.content
        tree = etree.HTML(html)
        ip_list = tree.xpath('//td[@data-title="IP"]/text()')
        port_list = tree.xpath('//td[@data-title="PORT"]/text()')
        for index, ip in enumerate(ip_list):
            plist.append(f'{ip}:{port_list[index]}')


def read_iplist():
    with open('daili.txt', 'r+') as f:
        ip_list = f.read().split('\n')
        plist.extend(ip_list)


# 检测IP是否可用
def check_ip(ip):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    proxies = {'http': f'http://{ip}', 'https': f'https://{ip}'}
    try:
        # 请求连接是否可以访问
        start_time = time.time()
        requests.get('http://www.baidu.com/', headers=headers, proxies=proxies, timeout=config['timeout'])
        end_time = time.time()
        run_time = end_time-start_time
        if config['is_fail_log']:
            print(f'success-{ip}--{int(run_time)}')
        if int(run_time) == 0:
            print(f'IP池检测:success-{ip}--{int(run_time)}')
        dlmysql.add('successstore', ip)
    except:
        if config['is_fail_log']:
            print(f'fail-{ip}')


def main():
    threads = []
    lock = Lock()
    for index, ip in enumerate(plist):
        time.sleep(1)
        lock.acquire()
        t = Proxies(ip)
        lock.release()
        threads.append(t)
        t.start()
    for index, t in enumerate(threads):
        t.join()


# 程序入口 接入代理只要把获取的IP列表装入plist即可
# xxxxx()
# main()此为一个完整的接口
if __name__ == '__main__':
    while True:
        getIplist()
        main()
        getKDLIpList()
        main()



