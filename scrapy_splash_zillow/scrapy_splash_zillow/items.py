# -*- coding: utf-8 -*-

import scrapy


class ZillowItem(scrapy.Item):
    home_price = scrapy.Field()
    zip_code = scrapy.Field()
