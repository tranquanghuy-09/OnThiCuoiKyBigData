# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Iuh20092731ScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    productUrl = scrapy.Field()
    title = scrapy.Field()
    decriptions = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    rating = scrapy.Field()
    