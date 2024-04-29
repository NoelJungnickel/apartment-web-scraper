import scrapy
import chompjs
import re

class FranzSpider(scrapy.Spider):
    name = "franz"
    allowed_domains = ["the-franz.com"]
    start_urls = ["https://the-franz.com/de/grundrisse/"]

    def parse(self, response):
        apartments_list = []

        for i in range(13, 19):
            string = "".join([s.strip() for s in response.css("script::text")[i].get().splitlines()])
            start = string.split("};", 1)[0].find("settings")
            end = string.find("};")
            string = string[start+len("settings"):end] + "}"
            string = string.split("=", 1)[1].strip()
            apartments_list.append(chompjs.parse_js_object(string))

        for i in range(len(apartments_list)):
            for j in range(len(apartments_list[i]["spots"])):
                if apartments_list[i]["spots"][j]["tooltip_content"]["squares_settings"]["containers"][0]["settings"]["elements"][0]["options"].get("text") != None:
                    apartment = apartments_list[i]["spots"][j]["tooltip_content"]["squares_settings"]["containers"][0]["settings"]["elements"][0]["options"].get("text").get("text")
                    location = re.search(r'<p>(\w+)', apartment).group(1)
                    number = re.search(r'- ([\d+\.]*\w+\*?)', apartment).group(1)
                    rooms = re.search(r'(\d+) Zimmer', apartment).group(1)
                    size = re.search(r'(\d+,\d+)', apartment).group(1)
                    floor = re.search(r'Zimmer / (\w+)', apartment).group(1)

                    if 'class="sc-state available"' in apartment:
                        status = "free"
                    else:
                        status = "sold/reserved"

                    yield {
                        "provider": "franz",
                        "location": location,
                        "number": number,
                        "rooms": rooms,
                        "size": size,
                        "price": "",
                        "status": status,
                        "floor": floor
                    }

        #Preis fehelt irgendwie? Ist nicht im Script zu finden