# -*- coding: utf-8 -*-
import os
from os import path

from scrapy.loader import ItemLoader

from hanman.items import HanmanItem
import scrapy
from scrapy.utils import spider
import requests


class ManhwaSpider(scrapy.Spider):
    name = 'manhwa'

    def start_requests(self):
        yield scrapy.Request(f'https://www.manhwa.cc/booklist/%E9%9F%A9%E5%9B%BD?tag=%E9%9F%A9%E5%9B%BD&page={self.page}')

    def parse(self, response):
        comics = response.xpath('//div[@class="m1100 l_content"]/ul/li')
        # next_page = response.xpath('//div[@class="pager"]/div[@class="pagination"]/a[@id="nextPage"]/@href').get()
        comic_urls = comics.xpath('a/@href').getall()
        # comic_names = comics.xpath('a/h3').getall()
        # comic_covers = comics.xpath('a/img/@data-original').getall()
        # comic_status = comics.xpath('a/p/i/text()').getall()
        # comic_update_times = comics.xpath('a/p/span/text()').getall()
        for index, comic_url in enumerate(comic_urls):
            yield response.follow(url=comic_url, callback=self.parse_chapter)

    def parse_chapter(self, response):
        charpters = response.xpath('//div[@class=$val]/ul/li', val='d_menu')
        charpter_urls = charpters.xpath('a/@href').getall()
        # charpter_name = charpters.xpath('a/b/text()').getall()
        for charpter_url in charpter_urls:
            yield response.follow(url=charpter_url, callback=self.parse_content)

    def parse_content(self, response):
        contents = response.xpath('//div[@class="m1100 m_content"]/div[@class="r_img "]/img/@data-original').getall()
        for index, content in enumerate(contents):
            item = HanmanItem()
            item['comic_name'] = response.xpath('//div[@class="m1100 m_content"]/div[@class="ov r_tab"]/div[@class="fl r_tab_l"]/b/text()').get()
            item['comic_chapter_name'] = response.xpath('//div[@class="m1100 m_content"]/div[@class="ov r_tab"]/div[@class="fl r_tab_l"]/span/text()').get()
            item['img'] = contents[index]
            item['i'] = index
            yield item




