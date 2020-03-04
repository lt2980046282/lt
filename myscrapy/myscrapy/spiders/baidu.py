# -*- coding: utf-8 -*-
import scrapy
from scrapy.utils import spider


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    title = ''
    headers ={
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36'
    }

    def start_requests(self):
        start_urls = [f'https://www.baidu.com/s?wd=终极斗罗']
        yield scrapy.Request(url=start_urls[0], callback=self.parse, headers=self.headers)

    def parse(self, response):
        res = response.xpath('//div[@id="wrapper_wrapper"]/div[@id="container"]/div[@id="content_left"]/div[@class]/h3')
        list_titles = res.xpath('string(.)').extract()
        list_urls = res.xpath('a/@href').getall()
        print(list_urls)
