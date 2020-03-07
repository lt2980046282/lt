import time
from threading import Thread

import requests
from lxml import etree
from app01.models import Store, SuccessStore, FailStore

class Proxies(Thread):
    success_ip_list = []
    fail_ip_list = []
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
    iplist = tree.xpath('//body/text()')
    del iplist[0]
    del iplist[0]
    iplist.pop()
    iplist[0] = iplist[0].replace('\n', '')
    return iplist


def check_ip(ip):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    Store(proxy=ip).save()
    proxies = {'http': f'http://{ip}', 'https': f'https://{ip}'}
    try:
        requests.get('https://www.baidu.com/s?wd=ip', headers=headers, proxies=proxies)
        # print(f'success-{ip}')
        SuccessStore(proxy=ip).save()
    except:
        # print(f'fail-{ip}')
        FailStore(proxy=ip).save()


def main():
    threads = []
    ip_list = getIplist()
    print(len(ip_list))
    for ip in ip_list:
        t = Proxies(ip)
        threads.append(t)
        t.start()
    for index, t in enumerate(threads):
        t.join()
        print(index)



main()



