# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class CheatsheetItem(Item):
    # define the fields for your item here like:
    # name = Field()
    #pass
    title = Field()
    link = Field()
    category = Field()
