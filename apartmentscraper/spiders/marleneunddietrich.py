import scrapy


class MarleneunddietrichSpider(scrapy.Spider):
    name = "marleneunddietrich"
    start_urls = ["https://navigator.beyonity.de/?id=A6C545DB"]

    def parse(self, response):
        apartments_list = response.css("ul::text").getall()

        for i in range(len(apartments_list)):
            yield {
                "provider": "marleneunddietrich",
                "text": apartments_list[i],
            }
