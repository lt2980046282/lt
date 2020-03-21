import scrapy
from novel.items import JMSWItem


class JMSW(scrapy.Spider):
    name = 'zxw'

    def start_requests(self):
        yield scrapy.Request(url=f'https://www.48wx.org/wanben/1_{self.page}')

    def parse(self, response):
        novel_items = response.xpath('//div[@class="l"]/ul/li')
        for novel_item in novel_items:
            item = JMSWItem()
            item['novel_name'] = novel_item.xpath('span[@class="s2"]/a/text()').get()
            novel_url = novel_item.xpath('span[@class="s2"]/a/@href').get()
            item['author'] = novel_item.xpath('span[@class="s5"]/text()').get()
            yield response.follow(url=novel_url, meta={"item": item}, callback=self.parse_chapter)

    def parse_chapter(self, response):
        chapter_items = response.xpath('//div[@id="list"]/dl/dd')
        for chapter_item in chapter_items:
            item = response.meta['item']
            item['chapter_name'] = chapter_item.xpath('a/text()').get()
            chapter_url = chapter_item.xpath('a/@href').get()
            yield response.follow(url=chapter_url, meta={"item": item}, callback=self.parse_content)

    def parse_content(self, response):
        item = response.meta['item']
        item['content'] = response.xpath('//div[@id="content"]').get()
        # items = response.xpath('//title/text()').get()
        # ary = str(items).split('_')
        # item['chapter_name'] = ary[0]
        # item['novel_name'] = ary[1]
        yield item