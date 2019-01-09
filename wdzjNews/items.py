# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WdzjnewsItem(scrapy.Item):
    # 消息标题
    news_title = scrapy.Field()
    # 消息详情
    news_subMessage = scrapy.Field()
    # 消息来源
    news_source = scrapy.Field()
    # 消息标题
    news_time = scrapy.Field()
