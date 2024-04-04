import scrapy


class MarleneunddietrichSpider(scrapy.Spider):
    name = "marleneunddietrich"
    allowed_domains = ["marleneunddietrich.de"]
    start_urls = ["https://marleneunddietrich.de/"]

    def parse(self, response):
        apartments = response.css("div.bvr-ui-sidebar__list-item")

        for apartment in apartments:
            yield {
                "location": [],
                "number": apartment.css(".bvr-ui-sidebar__list-item__header h2 span::text").extract(),
                "rooms": apartment.css(".bvr-ui-sidebar__list-item__meta ul li[3] <-mika fragen span::text").extract(),
                "size": apartment.css(".bvr-ui-sidebar__list-item__meta ul li[1] <-mika fragen span::text").extract(),
                "price": apartment.css(".bvr-ui-sidebar__list-item__header .bvr-ui-sidebar__list-item__badge .bvr-ui-sidebar__list-item__badge-label::text").extract(),
                "status": apartment.css(".bvr-ui-sidebar__list-item__header .bvr-ui-sidebar__list-item__badge .bvr-ui-sidebar__list-item__badge-circle::style").extract(),
                "floor": apartment.css(".bvr-ui-sidebar__list-item__meta ul li[2] <-mika fragen span::text").extract(),
            }


        #for apartment in response.css("div.bvr-ui-sidebar__list-item"):
        #    yield {
        #        "apartment": apartment.css(".bvr-ui-sidebar__list-item::text").extract(),
        #    }
