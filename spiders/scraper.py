import scrapy
from scrapy.shell import inspect_response
import sys
import re
import time
import datetime
import json
from ..items import ClothItem


class VintedSpider(scrapy.Spider):
    name = "vinted_spider"
    start_urls = [
        "https://www.vinted.fr/api/v2/items?catalog_ids=5&page=2&per_page=96",
    ]

    # Categories IDs Memo:
    # Men: 5
    # Women: 1904
    # Children: 1193

    z = 2

    def parse(self, response):

        jsonresponse = json.loads(response.text)
        item = ClothItem()

        for i in range(96):
            print(jsonresponse["items"][i]["path"].split("/")[1])
            item["cloth_type"] = jsonresponse["items"][i]["path"].split("/")[1]
            item["brandname"] = jsonresponse["items"][i]["brand"]
            item["first_image"] = jsonresponse["items"][i]["photos"][0]["full_size_url"]
            try:
                item["second_image"] = jsonresponse["items"][i]["photos"][1][
                    "full_size_url"
                ]
            except IndexError:
                item["second_image"] = None
            yield item

            self.z += 1

            yield response.follow(
                "https://www.vinted.fr/api/v2/items??catalog_ids=5&page="
                + str(self.z)
                + "&per_page=96",
                callback=self.parse,
                dont_filter=True,
            )


class HMSpider(scrapy.Spider):
    name = "hm_spider"
    start_urls = [
        "https://www2.hm.com/en_gb/men/shop-by-product/view-all.html?sort=stock&image-size=small&image=model&offset=0&page-size=1623"
    ]

    def parse(self, response):
        SET_SELECTOR = ".product-item"
        item = ClothItem()

        for clothItem in response.css(SET_SELECTOR):
            print(clothItem)
            CLOTH_TYPE_SELECTOR = ".link::text"
            PRICE_SELECTOR = ".price.regular::text"
            FIRST_IMAGE_SELECTOR = ".//article/div[1]/a/img/@data-src"
            COLOURS_SELECTOR = ".//article/div[2]/ul/li[1]/a/text()"
            SECOND_IMAGE_SELECTOR = ".//article/div[1]/a/img/@data-altimage"

            item["cloth_type"] = clothItem.css(CLOTH_TYPE_SELECTOR).get()
            item["brandname"] = "H&M"
            item["price"] = clothItem.css(PRICE_SELECTOR).get()
            item["first_image"] = "https:" + str(
                clothItem.xpath(FIRST_IMAGE_SELECTOR).get()
            )
            item["second_image"] = (
                "https:" + clothItem.xpath(SECOND_IMAGE_SELECTOR).get()
            )
            item["gender"] = "men"
            item["colour"] = clothItem.xpath(COLOURS_SELECTOR).get()
            item["created_at"] = datetime.datetime.utcnow()
            yield item