# -*- coding: utf-8 -*-
import scrapy


class KuaidailiSpider(scrapy.Spider):
    name = 'daili'
    page = ''
    def start_requests(self):
        yield scrapy.Request(url=f'https://www.kuaidaili.com/free/intr/{self.page}')

    def parse(self, response):
        ip_list = response.xpath('//td[@data-title="IP"]/text()').getall()
        port_list = response.xpath('//td[@data-title="PORT"]/text()').getall()
        for index, ip in enumerate(ip_list):
            with open('daili.txt', 'a+') as f:
                f.write(f'{ip}:{port_list[index]}\n')

