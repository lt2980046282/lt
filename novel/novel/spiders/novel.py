# coding=gbk
import time
from novel.items import NovelItem
import scrapy

class ManhwaSpider(scrapy.Spider):
    page = 1
    book = 0
    name = 'novel'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }

    def start_requests(self):
        yield scrapy.Request(f'http://www.biquge.info/wanjiexiaoshuo/{self.page}', meta={'book': self.book})

    def parse(self, response):
        book = int(response.meta['book'])
        item = NovelItem()
        item['novel_name'] = response.xpath('//span[@class="s2"]/a/text()')[book].getall()
        item['type'] = response.xpath('//span[@class="s1"]/text()')[book].get()
        item['author'] = response.xpath('//span[@class="s4"]/text()')[book].get()
        url = response.xpath('//span[@class="s2"]/a/@href')[book].get()
        yield response.follow(url=url, meta={'item': item}, callback=self.parse_chapter)

    def parse_chapter(self, response):
        charpters = response.xpath('//div[@id=$val]/dl/dd', val='list')
        item = dict(response.meta['item'])
        for charpter in charpters:
            item = dict(response.meta['item'])
            item['chapter_name'] = charpter.xpath('a/text()').get()
            url = charpter.xpath('a/@href').get()
            yield response.follow(url=url, meta={'item': item}, callback=self.parse_content)

    def parse_content(self, response):
        item = dict(response.meta['item'])
        print(item)
        content = response.xpath('//div[@id="content"]')
        # 获取整个元素
        item['content'] = response.xpath('//div[@id="content"]').get()
        # 获取内容文本
        # item['content'] = content.xpath('string(.)').extract()
        yield item




