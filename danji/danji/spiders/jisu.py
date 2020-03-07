import scrapy
from danji.items import DanjiItem
from scrapy.loader import ItemLoader


class DanJi(scrapy.Spider):
    name = 'jisu'
    page = 1

    def start_requests(self):
        yield scrapy.Request(url=f'https://dl.3dmgame.com/')

    def parse(self, response):
        items = response.xpath('//div[@class="item"]/a')
        url = items[0].xpath('@href').get()
        url = str(url).replace('https://dl.3dmgame.com/pc/', '')
        url = url.replace('.html', '')
        for index in range(21751, int(url)):
            print(index)
            yield response.follow(url=f'http://box.hyds360.com/down/{index}-2.html', callback=self.parse_content)

    def parse_content(self, response):
        item = DanjiItem()
        item['name'] = response.xpath('//li[@class="gameID_cn"]/text()').get()
        item['size'] = response.xpath('//li[@class="gameSize"]/span/text()').get()
        item['download_name'] = response.xpath('//div[@class="n1_content"]/a/text()').getall()
        item['download_url'] = response.xpath('//div[@class="n1_content"]/a/@href').getall()
        if len(item['download_name']) >0:
            yield item

