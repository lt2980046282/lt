# coding=gbk
import time

from novel.items import NovelItem
import scrapy


class ManhwaSpider(scrapy.Spider):
    name = 'manhwa'
    author = ''
    novel_name = ''
    type = ''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    {}
    def start_requests(self):
        yield scrapy.Request(f'http://www.biquge.info/wanjiexiaoshuo/{self.page}')

    def parse(self, response):
        comic_urls = response.xpath('//span[@class="s2"]/a/@href').getall()
        for index, comic_url in enumerate(comic_urls):
            yield response.follow(url=comic_url, callback=self.parse_chapter, headers=self.headers)

    def parse_chapter(self, response):
        charpters = response.xpath('//div[@id=$val]/dl/dd', val='list')
        charpter_urls = charpters.xpath('a/@href').getall()
        self.novel_name = response.xpath('//div[@id="info"]/h1/text()').get()
        author = (response.xpath('//div[@id="info"]/p/text()').getall())[0]
        self.author = str(author).replace('作    者:', '')
        type = (response.xpath('//div[@id="info"]/p/text()').getall())[1]
        self.type = str(type).replace('类    别:', '')
        for charpter_url in charpter_urls:
            item = NovelItem()
            item['novel_name'] = self.novel_name
            item['url'] = charpter_url
            item['type'] = self.type
            item['author'] = self.author
            yield item
            # yield response.follow(url=charpter_url, callback=self.parse_content)

    # def parse_content(self, response):
    #     item = NovelItem()
    #     item['chapter_name'] = response.xpath('//div[@class="bookname"]/h1/text()').get()
    #     content = response.xpath('//div[@id="content"]')
    #     item['content'] = content.xpath('string(.)').extract()
    #     item['author'] = self.author
    #     item['novel_name'] = self.novel_name
    #     item['type'] = self.type
    #     yield item




