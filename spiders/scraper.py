import scrapy
from scrapy.shell import inspect_response
import sys
import re
import time
import datetime
import json
from ..items import EcommerceItem, ClothItem, CoconutCharcoalItem


class VintedSpider(scrapy.Spider):
    name = "vinted_spider"
    start_urls = ["https://www.vinted.fr/vetements?search_text=Jeans%20coupe%20droite"]

    z = 2
    a = 0

    vetements = [
        "jupes",
        "t-shirt+imprimé",
        "bikini",
        "bas+de+bikini",
        "bas+de+pyjama",
        "blazer",
        "blouse",
        "blouson",
        "blouson+bomber",
        "body",
        "brassière",
        "caleçon",
        "caleçon+de+bain",
        "cape",
        "casquette",
        "chaussettes",
        "chaussettes+de+sport",
        "chemise",
        "chemise+classique",
        "nuisette",
        "chemisier",
        "chino",
        "collants",
        "combinaison",
        "corset",
        "costume",
        "cravate",
        "doudoune",
        "débardeur",
        "gilet",
        "haut+de+bikini",
        "haut+de+pyjama",
        "jersey",
        "jean+bootcut",
        "jean+boyfriend",
        "jean+droit",
        "jean+flare",
        "jean+slim",
        "jeans+skinny",
        "jeans+fuselé",
        "jegging",
        "jupe+de+sport",
        "jupe+en+cuir",
        "jupe+en+jean",
        "jupe+longue",
        "jupe+plissée",
        "jupe+portefeuille",
        "jupe+trapèze",
        "legging",
        "lingerie",
        "maillot+de+bain",
        "manteau+classique",
        "manteau+court",
        "minijupe",
        "pantalon+3/4+de+sport",
        "pantalon+cargo",
        "pantalon+classique",
        "pantalon+de+costume",
        "pantalon+de+survêtement",
        "pantalon+en+cuir",
        "pantalons+outdoor",
        "parka",
        "peignoir",
        "polo",
        "porte-jarretelles",
        "pullover",
        "pyjama",
        "robe+chemise",
        "robe+d'été",
        "robe+de+cocktail",
        "robe+de+soirée",
        "robe+de+sport",
        "robe+en+jean",
        "robe+en+jersey",
        "robe+fourreau",
        "robe+longue",
        "robe+pull",
        "salopette",
        "short",
        "short+de+bain",
        "short+de+sport",
        "short+en+jean",
        "shorts+outdoor",
        "shorty",
        "slip",
        "slip+de+bain",
        "socquettes",
        "soutien-gorge+de+sport",
        "soutien-gorge+invisible",
        "soutien-gorge+push-up",
        "soutien-gorge+triangle",
        "soutien-gorge+à+armatures",
        "soutien-gorge+à+bretelles+amovibles",
        "string",
        "survêtement",
        "survêtement+en+néoprène",
        "sweat+polaire",
        "sweat+à+capuche",
        "sweatshirt",
        "t-shirt+basique",
        "t-shirt+de+sport",
        "t-shirt+de+surf",
        "t-shirt+imprimé",
        "t-shirt+à+manches+longues",
        "trench",
        "tunique",
        "veste+hardshell",
        "veste+coupe-vent",
        "veste+d'hiver",
        "veste+de+costume",
        "veste+de+running",
        "veste+de+survêtement",
        "veste+en+cuir",
        "veste+en+jean",
        "veste+en+similicuir",
        "veste+imperméable",
        "veste+légère",
        "veste+mi-saison",
        "veste+polaire",
        "veste+sans+manches",
    ]

    vetements_bis = [
        "Jupe",
        "T-shirt imprimé",
        "Bikini",
        "Bas de bikini",
        "Bas de pyjama",
        "Blazer",
        "Blouse",
        "Blouson",
        "Blouson bomber",
        "Body",
        "Brassière",
        "Caleçon",
        "Caleçon de bain",
        "Cape",
        "Caraco",
        "Casquette",
        "Chaussettes",
        "Chaussettes de sport",
        "Chemise",
        "Chemise classique",
        "Chemise de nuit / nuisette",
        "Chemisier",
        "Chino",
        "Collants",
        "Combinaison",
        "Corset",
        "Costume",
        "Cravate",
        "Doudoune",
        "Débardeur",
        "Gilet",
        "Haut de bikini",
        "Haut de pyjama",
        "Jersey",
        "Jean bootcut",
        "Jean boyfriend",
        "Jean droit",
        "Jean flare",
        "Jean slim",
        "Jeans skinny",
        "Jeans fuselé",
        "Jegging",
        "Jupe de sport",
        "Jupe en cuir",
        "Jupe en jean",
        "Jupe longue",
        "Jupe plissée",
        "Jupe portefeuille",
        "Jupe trapèze",
        "Legging",
        "Lingerie",
        "Maillot de bain",
        "Manteau classique",
        "Manteau court",
        "Minijupe",
        "Pantalon 3/4 de sport",
        "Pantalon cargo",
        "Pantalon classique",
        "Pantalon de costume",
        "Pantalon de survêtement",
        "Pantalon en cuir",
        "Pantalons outdoor",
        "Parka",
        "Peignoir",
        "Polo",
        "Porte-jarretelles",
        "Pullover",
        "Pyjama",
        "Robe chemise",
        "Robe d'été",
        "Robe de cocktail",
        "Robe de soirée",
        "Robe de sport",
        "Robe en jean",
        "Robe en jersey",
        "Robe fourreau",
        "Robe longue",
        "Robe pull",
        "Salopette",
        "Short",
        "Short de bain",
        "Short de sport",
        "Short en jean",
        "Shorts outdoor",
        "Shorty",
        "Slip",
        "Slip de bain",
        "Socquettes",
        "Soutien-gorge de sport",
        "Soutien-gorge invisible",
        "Soutien-gorge push-up",
        "Soutien-gorge triangle",
        "Soutien-gorge à armatures",
        "Soutien-gorge à bretelles amovibles",
        "String",
        "Survêtement",
        "Survêtement en néoprène",
        "Sweat polaire",
        "Sweat à capuche",
        "Sweatshirt",
        "T-shirt basique",
        "T-shirt de sport",
        "T-shirt de surf",
        "T-shirt imprimé",
        "T-shirt à manches longues",
        "Trench",
        "Tunique",
        "Veste hardshell",
        "Veste coupe-vent",
        "Veste d'hiver",
        "Veste de costume",
        "Veste de running",
        "Veste de survêtement",
        "Veste en cuir",
        "Veste en jean",
        "Veste en similicuir",
        "Veste imperméable",
        "Veste légère",
        "Veste mi-saison",
        "Veste polaire",
        "Veste sans manches",
    ]

    def parse(self, response):
        try:
            jsonresponse = json.loads(response.text)
            item = ClothItem()

            for i in range(24):
                try:
                    item["name"] = self.vetements_bis[self.a]
                except:
                    print("Here is the fucking issue: ", sys.exc_info()[0])
                item["brandname"] = jsonresponse["items"][i]["brand"]
                item["first_image"] = jsonresponse["items"][i]["photos"][0][
                    "full_size_url"
                ]
                try:
                    item["second_image"] = jsonresponse["items"][i]["photos"][1][
                        "full_size_url"
                    ]
                except IndexError:
                    item["second_image"] = None
                yield item

            self.z += 1

            try:
                yield response.follow(
                    "https://www.vinted.fr/api/v2/items?search_text="
                    + self.vetements[self.a]
                    + "&catalog_ids=5&page="
                    + str(self.z)
                    + "&per_page=24",
                    callback=self.parse,
                    dont_filter=True,
                )
                """ if self.z > 10 """
            except:
                self.a += 1
                yield response.follow(
                    "https://www.vinted.fr/api/v2/items?search_text="
                    + self.vetements[self.a]
                    + "&catalog_ids=5&page="
                    + str(self.z)
                    + "&per_page=24",
                    callback=self.parse,
                    dont_filter=True,
                )
        except:
            yield response.follow(
                "https://www.vinted.fr/api/v2/items?search_text="
                + self.vetements[self.a]
                + "&catalog_ids=5&page="
                + str(self.z)
                + "&per_page=24",
                callback=self.parse,
                dont_filter=True,
            )


class HMSpider(scrapy.Spider):
    name = "hm_spider"
    start_urls = [
        "https://www2.hm.com/en_gb/men/shop-by-product/view-all.html?sort=stock&image-size=small&image=model&offset=0&page-size=16"
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