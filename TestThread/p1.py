import time

import requests
from lxml import etree
import threading
from queue import Queue


class QiubaiSpider:
    def __init__(self):
        self.url = 'https://www.baidu.com/s?wd=ip'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
        }
        self.ip_queue = Queue()
        self.ip_queue = self.getIpList()

    def getIpList(self):
        ip_queue = Queue()
        response = requests.get('http://www.89ip.cn/tqdl.html?api=1&num=9999')
        response.encoding = 'utf-8'
        html = response.content
        tree = etree.HTML(html)
        iplist = tree.xpath('//body/text()')
        del iplist[0]
        del iplist[0]
        iplist.pop()
        iplist[0] = iplist[0].replace('\n', '')
        for ip in iplist:
            self.ip_queue.put(ip)
        return ip_queue


    def tstart(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
        }
        while True:
            url = self.ip_queue.get()
            proxies = {'http': f'http://{url}', 'https': f'https://{url}'}
            try:
                requests.get('https://www.baidu.com/s?wd=ip', headers=headers, proxies=proxies, timeout=3)
                print(f'success-{url}')
            except:
                print(f'fail-{url}')


    def run(self):
        thread_list = []
        for i in range(300):  # 请求阶段开启多个线程
            t_parse = threading.Thread(target=self.tstart)
            thread_list.append(t_parse)
        for t in thread_list:
            t.setDaemon(True)  # 把子线程设置为守护线程，该线程不重要，主线程结束==子线程结束
            t.start()
        for q in [self.ip_queue]:
            q.join()



if __name__ == '__main__':
    qiu = QiubaiSpider()
    print(qiu.ip_queue)
    qiu.run()
