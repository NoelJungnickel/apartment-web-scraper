import scrapy


class ApartmentsSpider(scrapy.Spider):
    name = "apartments"
    allowed_domains = ["ba94.de"]
    start_urls = [
        "https://ba94.de/en/wohnungsuebersicht/",
    ]

    def parse(self, response):
        apartments = response.css("div.elementor")

        for apartment in apartments:
            yield {
                "location": apartment.css("td::text").getall(),
                "number": apartment.css("td::text").getall(),
                "rooms": apartment.css("td::text").getall(),
                "size": apartment.css("td::text").getall(),
                "price": apartment.css("td::text").getall(),
                "status": apartment.css("td::text").getall(),
            }

        #apartment_data = ApartmentscraperItem()
        #apartment_data["location"] = response.css("td::text").getall(),
        #apartment_data["number"] = response.css("td::text").getall(),
        #apartment_data["rooms"] = response.css("td::text").getall(),
        #apartment_data["size"] = response.css("td::text").getall(),
        #apartment_data["price"] = response.css("td::text").getall(),
        #apartment_data["status"] = response.css("td::text").getall()

        #yield apartment_data

        #for apartment in response.css("div.elementor"):
        #    yield {
        #        "td": apartment.css("td::text").getall(),
        #    }