import time
import random
import numpy as np
import scrapy


class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    start_urls = ['http://www.xbiquge.la/xiaoshuodaquan/']
    novel_name = ''
    headers = {
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }
    def start_requests(self):

        yield scrapy.Request(url=self.start_urls[0], callback=self.parse, headers=self.headers)

    def parse(self, response):
        list = response.xpath('//div[@id="main"]/div[@class="novellist"]/ul/li')
        novellist = []
        chapter_urls = []
        for index, li in enumerate(list):
            model = NovelModel()
            novel_url = li.xpath('a/@href').get()
            novel_name = li.xpath('a/text()').get()
            self.novel_name = novel_name
            model.novel_url = novel_url
            model.novel_name = novel_name
            novellist.append(model)
            yield response.follow(novel_url, callback=self.parse_chapter, headers=self.headers)

    def parse_chapter(self, response):
        list = response.xpath('//div[@class="box_con"]/div[@id="list"]/dl/dd/a')
        chapters = []
        for index, li in enumerate(list):
                chapter_url = li.xpath('@href').get()
                chapter_name = li.xpath('text()').get()
                chapters.append({
                    'chapter_url': chapter_url,
                    'chapter_name': chapter_name,
                })
                if int(index % 2) == 1:
                    time.sleep(2
                               )
                    yield response.follow(chapter_url, callback=self.parse_content, headers=self.headers)
                else:
                    yield response.follow(chapter_url, callback=self.parse_content, headers=self.headers)

    def parse_content(self, response):

        list = response.xpath('//div[@class="content_read"]/div[@class="box_con"]/div[@id="content"]')
        name = response.xpath('//div[@class="content_read"]/div[@class="box_con"]/div[@class="bookname"]/h1/text()').get()
        with open(f"novel/{self.novel_name}.txt", "a+") as f:
            f.write(f'{name}:{list.xpath("string(.)").extract()}\n')


class NovelModel:
    def to_string(self):
        return self.novel_name

    novel_url = ''
    novel_name = ''
    chapters = []
    contents = []
    author = ''


class NovelChapterNameAndChapterUrl:
    chapter_name = ''
    chapter_url = ''
