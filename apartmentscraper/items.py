import scrapy

class ApartmentscraperItem(scrapy.Item):
    location = scrapy.Field()
    number = scrapy.Field()
    rooms = scrapy.Field()
    size = scrapy.Field()
    price = scrapy.Field()
    status = scrapy.Field()
    floor = scrapy.Field()
