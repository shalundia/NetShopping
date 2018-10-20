# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join
from scrapy.loader.processors import Compose


def remove_space(item):
    x=''.join(item)
    x=x.strip()
    return None if x=='' else x

class NetshoppingItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    keyword = scrapy.Field()
    name=scrapy.Field(input_processor=Compose(remove_space),
        output_processor=Join(),)
    price=scrapy.Field()
    shop_name=scrapy.Field(input_processor=Compose(remove_space),
        output_processor=Join(),)
    shop_url=scrapy.Field()
    item_url=scrapy.Field()
    
    
