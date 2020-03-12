import os
from threading import Thread


class RunSpider(Thread):
    def __init__(self, page):
        self.page = page
        super(RunSpider, self).__init__()
    def run(self):
        novel(self.page)


def novel(page):
    os.system(f'scrapy crawl novel -a page={page} -o novel{page}.json --nolog')
    print(page)


def daili():
    for index in range(1502):
        os.system(f'scrapy crawl daili -a page={index+1819} ')


def main():
    for index in range(200, 250):
        t = RunSpider(index)
        t.start()


if __name__ == '__main__':
    main()