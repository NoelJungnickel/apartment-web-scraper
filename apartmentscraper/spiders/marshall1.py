import scrapy

class Marshall1Spider(scrapy.Spider):
    name = "marshall1"
    allowed_domains = ["marshall1.de"]
    start_urls = ["https://www.marshall1.de/de/portfolio/grundrisse/"]

    def parse(self, response):
        apartments_list = []
        test = response.css("rs-layer")
        yield {"test": test.getall()}

        """for apartment in response.css("rs-modal-fullscreen"):
            apartments_list.append(apartment.css("td::text").extract())

        for i in range(len(apartments_list)):
            yield {
                "provider": "ba94",
                "location": apartments_list[i][0],
                "number": apartments_list[i][1],
                "rooms": apartments_list[i][2],
                "size": apartments_list[i][3],
                "price": apartments_list[i][4],
                "status": apartments_list[i][5],
                "floor": "",
            }"""