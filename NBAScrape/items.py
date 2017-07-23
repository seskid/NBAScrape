# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NbascrapeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    FirstName=scrapy.Field()
    LastName=scrapy.Field()
    Salary=scrapy.Field()
    TeamID=scrapy.Field()
    


