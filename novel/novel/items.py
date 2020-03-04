# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    # content = scrapy.Field()
    author = scrapy.Field()
    # chapter_name = scrapy.Field()
    novel_name = scrapy.Field()
    type = scrapy.Field()
    url = scrapy.Field()
    pass
