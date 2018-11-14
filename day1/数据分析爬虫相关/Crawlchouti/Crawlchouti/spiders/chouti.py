# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class ChoutiSpider(CrawlSpider):
    name = 'chouti'
    start_urls = ['https://dig.chouti.com/r/scoff/hot/1']

    # 实例化了一个链接提取器对象：allow：正则表达式
    # 作用：将起始url对应的页面数据中符合allow指定的正则表达式的链接进行提取
    link = LinkExtractor(allow=r'/r/scoff/hot/\d+')
    rules = (
        # Rule规则解析器
        # 作用：可以将连接提取器提取到的链接对应的页面数据进行指定规则的数据进行解析
        # 参数follow作用：将连接提取器继续作用到连接提取器提取出的链接所对应的页面中
        Rule(link, callback='parse_item', follow=True),
    )
    def parse_item(self, response):
        print(response.text)
