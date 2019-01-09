# -*- coding: utf-8 -*-
import scrapy
from wdzjNews.items import WdzjnewsItem


class WdzjnewsSpiderSpider(scrapy.Spider):
    name = 'wdzjnews_spider'
    allowed_domains = ['www.wdzj.com']
    start_urls = ['https://www.wdzj.com/news/hangye/']

    def parse(self, response):
        news_list = response.xpath("//ul[@class='zllist']/li")
        for i_item in news_list:
            news_item = WdzjnewsItem()
            info = i_item.xpath(".//div[@class='text']/h3/a/text()").extract_first()
            news_item['news_title'] = info.replace("\n","").replace(" ","").replace("\r","")
            # data = i_item.xpath(".//div[@class='text']/p/a[descendant-or-self::text()]")
            news_item['news_subMessage'] = i_item.xpath(".//div[@class='text']/p/a/text()").extract_first()
            news_item['news_source'] = i_item.xpath(".//div[@class='userxx']//div[@class='lbox']//span[1]/text()").extract_first()
            news_item['news_time'] = i_item.xpath(".//div[@class='userxx']//div[@class='lbox']//span[2]/text()").extract_first()
            yield news_item



        pageCount = int(response.xpath("//div[@class='pagebox']/em/strong[3]/text()").extract_first())
        for i in range(2,4):
            next_link = response.xpath( "//div[@class='pagebox']/a/@href" ).extract_first()
            if next_link:
                yield scrapy.Request( "https://www.wdzj.com/" + next_link +"p%s.html"%i, callback=self.parse )






