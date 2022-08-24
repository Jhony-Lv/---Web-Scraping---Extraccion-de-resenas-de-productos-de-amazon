# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Prueba0Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #Info del producto
    nombre = scrapy.Field()
    precio = scrapy.Field()
    envio = scrapy.Field()

    estrellas = scrapy.Field()

    #Info de la tienda
    nom_tienda = scrapy.Field()
    url_tienda = scrapy.Field()
    pass
