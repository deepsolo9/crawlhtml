#-*- coding: UTF-8 -*-
import pymongo
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from translation import Translation

class CrawlhtmlPipeline(object):

    t = Translation()
    
    def __init__(self):
        connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        if not item or item['content'] == '':
            valid = False
            raise DropItem("Missing content of page from %s" % (getattr(item, 'url', '')))
        else:
            new_text = CrawlhtmlPipeline.t.translateTxt(item['content'])
            item['content'] = new_text
        if valid:
            self.collection.insert(dict(item))
        return item
