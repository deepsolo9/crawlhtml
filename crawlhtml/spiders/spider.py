#-*- coding: UTF-8 -*-
from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.conf import settings
from crawlhtml.items import Page
from goose import Goose

class MainSpider(CrawlSpider):

    name = "spider"

    g = Goose()
    
    start_urls = ['http://www.usnews.com']
    allowed_domains = ['usnews.com']
    rules = [Rule(SgmlLinkExtractor(), callback='parse_item', follow=True)]
    
    def parse_item(self, response):
    
        article = MainSpider.g.extract(url=response.url)
        content = article.cleaned_text
        if content:
            page = Page()
            page['url'] = response.url
            page['title'] = article.title
            page['content'] = article.cleaned_text
    
            return page

        return None