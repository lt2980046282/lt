import os
import os
from threading import Thread


class RunSpider(Thread):
    def __init__(self, page):
        self.page = page
        super(RunSpider, self).__init__()

    def run(self):
        hanhua(self.page)


def hanhua(page):
    os.system(f'scrapy crawl manhwa -a page={page} -o manhua{page}.json --nolog')
    print(page)


def main():
    for index in range(26):
        t = RunSpider(index + 1)
        t.start()


if __name__ == '__main__':
    main()
