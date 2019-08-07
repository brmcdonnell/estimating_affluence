# -*- coding: utf-8 -*-
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose
from scrapy.spiders import Spider
from items import ZillowItem


class ZillowSpider(Spider):
    name = 'zillow'
    allowed_domains = ['zillow.com']
    start_urls = ['http://zillow.com/']
    url = start_urls[0] + 'homes/60464_rb/1_p'
    headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
               'accept-encoding': 'gzip, deflate, sdch, br',
               'accept-language': 'en-GB,en;q=0.8,en-US;q=0.6,ml;q=0.4',
               'cache-control': 'max-age=0',
               'upgrade-insecure-requests': '1',
               'user-agent': 'Chrome/74.0.3729.131'}
    
    def start_requests(self):
        pass
   
    def parse(self, response):
        item = ZillowItem()
        
#        for home in response.css():
#            item['zip_code'] = 
#            item['price']    = 
        return item
