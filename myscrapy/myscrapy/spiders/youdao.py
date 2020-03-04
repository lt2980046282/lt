import scrapy


class YoudaoSpider(scrapy.Spider):
    # name = 'youdao'
    names = ['a']
    start_urls = [f'http://www.youdao.com/w/eng/{names[0]}']

    def parse(self, response):
        # ??????????????
        list = response.xpath('//div[@class="wt-container"]/ul[@class="ol"]/li')
        for li in list:
            collinsMajorTran = li.xpath('div[@class="collinsMajorTrans"]/p')
            collinsMajorTran = collinsMajorTran.xpath('string(.)').extract()[0]
            collinsMajorTran = str(collinsMajorTran).replace('\n', '')
            collinsMajorTran = collinsMajorTran.replace('\t', '')
            collinsMajorTran = collinsMajorTran.replace('\r', '')
            collinsMajorTran = collinsMajorTran.replace('               ', '')
            collinsMajorTran = collinsMajorTran.strip()
            exampleLists = li.xpath('div[@class="exampleLists"]/div[@class="examples"]/p/text()').getall()
            print(exampleLists)
            with open('youdao.txt', 'a+') as f:
                f.write(f'{collinsMajorTran}\n')
            for exampleList in exampleLists:
                with open('youdao.txt', 'a+') as f:
                    f.write(f'{exampleList}\n')
        # #????
        # trans_container = response.xpath('//div[@class="trans-container"]/ul/li')
        # trans_container = trans_container.xpath('string(.)').extract()[0]
        # print(trans_container)
        # #???????
        # wordGroups = response.xpath('//div[@id="wordGroup2"]/p')
        # for wordGroup in wordGroups:
        #     wordGroup = wordGroup.xpath('string(.)').extract()[0]
        #     wordGroup = str(wordGroup).replace('\n', '')
        #     wordGroup = wordGroup.replace('\t', '')
        #     wordGroup = wordGroup.replace('\r', '')
        #     wordGroup = wordGroup.replace(' ', '')
        #     # wordGroup = wordGroup.strip()
        #     print(wordGroup)