# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ClothItem(scrapy.Item):
    # define the fields for your item here like:
    cloth_type = scrapy.Field()
    brandname = scrapy.Field()
    price = scrapy.Field()
    first_image = scrapy.Field()
    second_image = scrapy.Field()
    gender = scrapy.Field()
    colour = scrapy.Field()
    created_at = scrapy.Field()

    pass
