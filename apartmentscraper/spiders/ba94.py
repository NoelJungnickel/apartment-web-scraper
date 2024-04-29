import scrapy

class Ba94Spider(scrapy.Spider):
    name = "ba94"
    allowed_domains = ["ba94.de"]
    start_urls = ["https://ba94.de/en/wohnungsuebersicht/"]

    def parse(self, response):
        apartments_list = []

        for apartment in response.css("tr"):
            apartments_list.append(apartment.css("td::text").extract())

        for i in range(len(apartments_list)):
            apartments_list[i] = apartments_list[i][1:]
        
        apartments_list_temp = apartments_list.copy()
        for i in range(len(apartments_list)):
            if len(apartments_list[i]) < 2:
                apartments_list_temp.remove(apartments_list[i])
        apartments_list = apartments_list_temp.copy()

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
            }