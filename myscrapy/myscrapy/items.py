import scrapy


class NovelItem(scrapy.Item):
    #小说名称
    novel_name = scrapy.Field()
    #作者
    author = scrapy.Field()
    #小说章节名称列表
    chapter_name = scrapy.Field()
    #小说章节链接
    chapter_url = scrapy.Field()