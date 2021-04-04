# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import psycopg2


class WebscrappingPipeline:
    def process_item(self, item, spider):
        return item


class ClothsPipeline(object):
    """Cloths pipeline for storing scraped items in the database"""

    def open_spider(self, spider):
        hostname = "localhost"
        username = "nicolas"
        password = ""
        database = "lapenderie"
        self.connection = psycopg2.connect(
            host=hostname, user=username, password=password, dbname=database
        )
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute(
                "insert into cloths(brandlogourl,price,promo,href,brandname,first_image,name,second_image,categories,gender,colour,created_at,modified_at) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    item["brandlogourl"],
                    item["price"],
                    item["promo"],
                    item["href"],
                    item["brandname"],
                    item["first_image"],
                    item["name"],
                    item["second_image"],
                    item["categories"],
                    item["gender"],
                    item["colour"],
                    item["created_at"],
                    item["modified_at"],
                ),
            )
            self.connection.commit()
        except:
            self.connection.rollback()
            raise

        return item


class TrainingClothsPipeline(object):
    """Training cloths pipeline for storing scraped items in the database in order to train the AI on them later on"""

    def open_spider(self, spider):
        hostname = "localhost"
        username = "nicolas"
        password = ""
        database = "lapenderie"
        self.connection = psycopg2.connect(
            host=hostname, user=username, password=password, dbname=database
        )
        self.cur = self.connection.cursor()

    def close_spider(self, spider):
        self.cur.close()
        self.connection.close()

    def process_item(self, item, spider):
        try:
            self.cur.execute(
                "insert into training_cloths(brandname,first_image,name,second_image) values(%s,%s,%s,%s)",
                (
                    item["brandname"],
                    item["first_image"],
                    item["name"],
                    item["second_image"],
                ),
            )
            self.connection.commit()
        except:
            self.connection.rollback()
            raise

        return item
