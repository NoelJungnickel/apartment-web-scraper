import scrapy


class Ba94Spider(scrapy.Spider):
    name = "ba94"
    allowed_domains = ["ba94.de"]
    start_urls = ["https://ba94.de/en/wohnungsuebersicht/"]

    def parse(self, response):
        apartments = response.css("tr")

        for apartment in apartments:
            yield {
                "location": apartment.css("td.column-lageimobjekt::text").extract(),
                "number": apartment.css("td.column-wohnungsnummer::text").extract(),
                "rooms": apartment.css("td.column-zimmer::text").extract(),
                "size": apartment.css("td.column-wohnflcheinm::text").extract(),
                "price": apartment.css("td.column-kaufpreisgesamt::text").extract(),
                "status": apartment.css("td.column-status::text").extract(),
                "floor": [],
            }

        #for apartment in response.css("tr"):
        #    yield {
        #        "apartment": apartment.css("td::text").extract(),
        #    }