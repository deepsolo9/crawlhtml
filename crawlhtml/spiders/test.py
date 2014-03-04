from scrapy.spider import Spider
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy.conf import settings

class A(object):
	num = 0

class DmozSpider(CrawlSpider):

    name = "test"
    
    start_urls = ['http://www.usnews.com'] # urls from which the spider will start crawling
    rules = [Rule(SgmlLinkExtractor(), callback='parse_item', follow=True)]
    
    def parse_item(self, response):
    	A.num += 1
    	print '######', A.num, ':', response.url
