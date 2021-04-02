# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CoconutCharcoalItem(scrapy.Item):
    # define the fields for your item here like:
    Entreprise = scrapy.Field()
    Number = scrapy.Field()
    pass


class EcommerceItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    brandname = scrapy.Field()
    brandlogourl = scrapy.Field()
    price = scrapy.Field()
    promo = scrapy.Field()
    first_image = scrapy.Field()
    second_image = scrapy.Field()
    href = scrapy.Field()
    gender = scrapy.Field()
    categories = scrapy.Field()
    colour = scrapy.Field()
    created_at = scrapy.Field()
    modified_at = scrapy.Field()
    pass


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
