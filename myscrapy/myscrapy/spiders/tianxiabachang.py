import time
from myscrapy.items import NovelItem
import scrapy


class TianxiabachangSpider(scrapy.Spider):
    name = 'tianxiabachang'
    basic_url = 'http://www.tianxiabachang.cn'
    start_urls = [f'{basic_url}/quanbu/']
    novel_name = ''
    author = ''
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, headers=self.headers)

    def parse(self, response):
        list = response.xpath('//div[@id="main"]/div[@class="novellist"]/ul/li')
        for index, li in enumerate(list):
            novel_url = li.xpath('a/@href').get()
            novel_name = li.xpath('a/text()').get()
            self.novel_name = novel_name
            yield response.follow(url=novel_url, callback=self.parse_chapter, headers=self.headers)

    def parse_chapter(self, response):
        list = response.xpath('//div[@class="box_con"]/div[@id="list"]/dl/dd/a')
        for index, li in enumerate(list):
            item = NovelItem()
            item['chapter_url'] = li.xpath('@href').get()
            item['chapter_name'] = li.xpath('text()').get()
            self.author = response.xpath('//div[@id="info"]/p/text()').get()
            item['author'] = self.author
            item['novel_name'] = self.novel_name
            yield item




