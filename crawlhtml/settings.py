#-*- coding: UTF-8 -*-
# Scrapy settings for crawlhtml project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'crawlhtml'

SPIDER_MODULES = ['crawlhtml.spiders']
NEWSPIDER_MODULE = 'crawlhtml.spiders'

ITEM_PIPELINES = {
    'crawlhtml.pipelines.CrawlhtmlPipeline': 10,
}

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "crawlhtml"
MONGODB_COLLECTION = "usnews"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'crawlhtml (+http://www.yourdomain.com)'
