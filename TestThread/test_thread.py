# encoding=gbk
import threading
from multiprocessing import Process

from lxml import etree

import requests


def getIpList():
    iplist = []
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


def tstart():
    for ip in getIpList():
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
        }
        proxies = {'http': f'http://{ip}', 'https': f'https://{1}'}
        try:
            requests.get('https://www.baidu.com/s?wd=ip', headers=headers, proxies=proxies, timeout=3)
            print(f'success-{ip}')
        except:
            print(f'fail-{ip}')

tstart()