import scrapy

class DanJi(scrapy.Spider):
    name = 'danji'
    page = 1

    def start_requests(self):
        yield scrapy.Request(url=f'https://dl.3dmgame.com/all_all_{self.page}_time/')

    def parse(self, response):
        base_url = ''
        items = response.xpath('//div[@class="item"]/a')
        for item in items:
            url = item.xpath('@href').get()
            url = str(url).replace('https://dl.3dmgame.com/pc/', 'http://box.hyds360.com/down/')
            url = url.replace('.html', '-2.html')
            # print(url)
            text = item.xpath('string(.)').extract()[0]
            print(text)
            if text == '暂无资源':
                print(text)
    #         else:
    #             yield response.follow(url=url, callback=self.parse_content)
    #
    # def parse_content(self, response):
    #     urls = response.xpath('//div[@class="infor"]/a/@href').getall()
    #     print(response.text)