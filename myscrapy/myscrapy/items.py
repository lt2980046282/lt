import scrapy


class NovelItem(scrapy.Item):
    #С˵����
    novel_name = scrapy.Field()
    #����
    author = scrapy.Field()
    #С˵�½������б�
    chapter_name = scrapy.Field()
    #С˵�½�����
    chapter_url = scrapy.Field()