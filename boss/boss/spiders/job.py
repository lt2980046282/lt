# -*- coding: utf-8 -*-
import scrapy
from boss.items import BossItem
from scrapy.loader import ItemLoader


class JobSpider(scrapy.Spider):
    name = 'job'
    import requests
    headers = {
        'authority': 'www.zhipin.com',
        'accept': '*/*',
        'sec-fetch-dest': 'empty',
        'x-requested-with': 'XMLHttpRequest',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'referer': 'https://www.zhipin.com/job_detail/?query=python&city=100010000&industry=&position=',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': '__c=1584710137; __g=-; lastCity=100010000; __l=l=https%3A%2F%2Fwww.zhipin.com%2Fweb%2Fcommon%2Fsecurity-check.html%3Fseed%3DEdGAGjN56gDBE%252BWGOzZNKWaib244NAuryn03mMI7w3w%253D%26name%3D3f4fd88c%26ts%3D1584710137435%26callbackUrl%3D%252Fjob_detail%252F%253Fquery%253Dpython%2526city%253D100010000%2526industry%253D%2526position%253D%26srcReferer%3D&r=&friend_source=0&friend_source=0; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1584710139; __zp_stoken__=4e5dfZzWyiohsfalVLjrQcffWWvl%2Bm0s3bdH5BmRM7wXUE3SQw%2FfraB6AZ9sIUQdYxjNYh6O224iJafgWk5%2F6oyvMF72YisQB4QQZONFX3N%2BNU24CzOwOSLVHosjHXnVwruB; __a=30844570.1584710137..1584710137.4.1.4.4; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1584710803; __zp_sseed__=EdGAGjN56gDBE+WGOzZNKUxe3NRNeh5WPPcFg8m9f7w=; __zp_sname__=3f4fd88c; __zp_sts__=1584710810680',
    }
    cookies = [
        {'domain': '.zhipin.com', 'httpOnly': False, 'name': '__l', 'path': '/', 'secure': False,
         'value': 'l=%2Fwww.zhipin.com%2Fweb%2Fcommon%2Fsecurity-check.html%3Fseed%3DEdGAGjN56gDBE%252BWGOzZNKeWOT9CXvuD5HYdAQjvyCI8%253D%26name%3D3f4fd88c%26ts%3D1584710292253%26callbackUrl%3D%252Fjob_detail%252F%253Fquery%253Dpython%2526city%253D100010000%2526industry%253D%2526position%253D%26srcReferer%3D&r=&friend_source=0'},
        {'domain': '.zhipin.com', 'httpOnly': False, 'name': '__g', 'path': '/', 'secure': False, 'value': '-'},
        {'domain': '.zhipin.com', 'expiry': 1900070292, 'httpOnly': False, 'name': '__a', 'path': '/', 'secure': False,
         'value': '45770166.1584710292..1584710292.1.1.1.1'},
        {'domain': '.zhipin.com', 'httpOnly': False, 'name': '__c', 'path': '/', 'secure': False, 'value': '1584710292'}
    ]

    def start_requests(self):
        yield scrapy.Request(url=f'https://www.zhipin.com/job_detail/?query={self.job_name}&city=100010000&industry=&position=', method='GET', headers=self.headers,cookies=self.cookies)

    def parse(self, response):
        item = BossItem()
        l = ItemLoader(item, response)
        l.add_xpath('company', '//a[@ka="jsearch_list_company_1_custompage"]')
        l.add_xpath('title', '//span[@class="job-name"]')
        l.add_xpath('address', '//span[@class="job-area"]')
        l.add_xpath('income', '//div[@class="job-limit clearfix"]/span[@class="red"]')
        l.add_xpath('experience', '//div[@class="job-limit clearfix"]/p')
        l.add_xpath('education', '//span[@class="job-area"]')
        url = response.xpath('//a[@ka="page-next"]/text()').get()
        yield l.load_item()
        print(response.text)
        # yield response.follow(url, callback=self.parse)
