# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.exceptions import DropItem

class CheatsheetPipeline(object):
    def process_item(self, item, spider):
        if item['link']:
            return item;
        else:
            raise DropItem()
