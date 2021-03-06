from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from cheatsheet.items import CheatsheetItem

class CheatsheetSpider(BaseSpider):
    name = "cheatsheet"
    allowed_domains = ["cheat-sheets.org"]
    start_urls = ["http://www.cheat-sheets.org/"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        sheets = []
        sections = hxs.select('//section[contains(@class,"cheatSheetsBlock")]')
        for section in sections:
            name = section.select('.//a/@id').extract()
            items = section.select('.//li[contains(@class,"itemLI")]')
            for item in items:
                sheet = CheatsheetItem()
                sheet['title'] = item.select('span/text()').extract()
                sheet['link'] = item.select('a[contains(@href,"saved")]/@href').extract()
                sheet['category'] = name
                sheets.append(sheet)
        return sheets
            
