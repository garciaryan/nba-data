# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayerStats(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    points = scrapy.Field()
    assists = scrapy.Field()
    rebounds = scrapy.Field()
    steals = scrapy.Field()
    blocks = scrapy.Field()
    turnovers = scrapy.Field()
    fgm = scrapy.Field()
    fga = scrapy.Field()
    threepm = scrapy.Field()
    threepa = scrapy.Field()
    minutes = scrapy.Field()
    pass

