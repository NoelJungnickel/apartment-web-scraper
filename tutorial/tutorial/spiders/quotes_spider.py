from pathlib import Path

import scrapy


class QuotesSpider(scrapy.Spider):
    name = "apartments"
    start_urls = [
        "https://ba94.de/en/wohnungsuebersicht/",
    ]

    def parse(self, response):
        for apartment in response.css("div.elementor"):
            yield {
                "td": apartment.css("td::text").getall(),
            }