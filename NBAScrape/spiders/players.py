import scrapy

from NBAScrape.items import NbascrapeItem

class PlayerSpider(scrapy.Spider):
    name = "player"
    
    def __init__(self,*a,**kw):
        self.start_urls = ['http://www.spotrac.com/nba/atlanta-hawks/cap/']

    def parse(self, response):
        item=NbascrapeItem()
        n=1;
        for player in response.css('td.player'):
            item['FirstName']=response.xpath('//child::td[1][contains(@class,"player")]/child::a/text()').extract()
            #item['LastName']=response.xpath('//child::div[2][contains(@class,"quote")]/child::span[contains(@class,"text")]/text()').extract()
            item['Salary']=response.xpath('//child::span[1][contains(@class,"cap info")]/text()').extract()
            #item['TeamID']=response.xpath('//child::div[2][contains(@class,"quote")]/child::span[contains(@class,"text")]/text()').extract()
            yield item
