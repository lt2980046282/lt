# -*- coding: utf-8 -*-
import scrapy
from yinghua.items import YinghuaItem


class FljtSpider(scrapy.Spider):
    name = 'fljt'
    page = 1

    def start_requests(self):
        yield scrapy.Request(url=f'https://www.fljt.win/page/{self.page}/')

    def parse(self, response):
        urls = response.xpath('//div[@class="post-list-item-container"]/a/@href').getall()
        for url in urls:
            yield response.follow(url=url,callback=self.parse_chapter)

    def parse_chapter(self, response):
        urls = response.xpath('//div[@class="post-content"]/p/img/@src').getall()
        for index, url in enumerate(urls):
            item = YinghuaItem()
            name = response.xpath('//div[@class="post-header-thumb-title"]/text()').get()
            item['name'] = str(name).replace('	', '')
            item['url'] = url
            item['i'] = index
            yield item