import scrapy
import chompjs

class Ba94Spider(scrapy.Spider):
    name = "amwinterfeldt"
    allowed_domains = ["amwinterfeldt.com"]
    start_urls = ["https://amwinterfeldt.com/grundrisse/"]

    def parse(self, response):
        """for s in response.css("style"):
            data = chompjs.parse_js_object(s.css("script::text").get())
            print(data)
            yield data"""
        javascript = response.css("script::text").get()
        data = chompjs.parse_js_object(javascript)
        yield data