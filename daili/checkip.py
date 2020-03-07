from threading import Thread

import requests


class CheckIP(Thread):
    def __init__(self, i):
        self.i = i
        super(CheckIP, self).__init__()

    def run(self):
        count = 0
        for i in range(155):
            for j in range(155):
                for k in range(155):
                    for l in range(155):
                        ip = f'{i+100}.{j+100}.{k+100}.{l+100}:{self.i}'
                        proxies = {'http': f'http://{ip}', 'https': f'https://{ip}'}
                        try:
                            requests.get('https://www.baidu.com', proxies=proxies, timeout=1)
                            print(f'success-{ip}')
                        except:
                            pass



def main():
    for m in range(6556):
        t = CheckIP(m)
        t.start()


if __name__ == '__main__':
    main()