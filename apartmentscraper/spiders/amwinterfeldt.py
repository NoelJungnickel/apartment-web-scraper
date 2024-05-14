import scrapy
import chompjs
import requests


class AmwinterfeldtSpider(scrapy.Spider):
    name = "amwinterfeldt"
    allowed_domains = ["amwinterfeldt.com"]
    start_urls = ["https://amwinterfeldt.com/grundrisse/"]
    request_url = "https://amwinterfeldt.com/wp-content/plugins/dh-slider-revolution-iframes//single_rev_slider.php?alias=h"

    def parse(self, response):
        apartments_list = []

        for i in range(7, 14):
            string = "".join(
                [s.strip() for s in response.css("script::text")[i].get().splitlines()]
            )
            start = string.split("};", 1)[0].find("settings")
            end = string.find("};")
            string = string[start + len("settings") : end] + "}"
            string = string.split("=", 1)[1].strip()
            apartments_list.append(chompjs.parse_js_object(string))

        yield {"test": apartments_list}

        for i in range(len(apartments_list)):
            for j in range(len(apartments_list[i]["spots"])):
                if (
                    apartments_list[i]["spots"][j]["tooltip_content"][
                        "squares_settings"
                    ]["containers"][0]["settings"]["elements"][0]["options"].get("text")
                    != None
                ):
                    apartment = (
                        apartments_list[i]["spots"][j]["tooltip_content"][
                            "squares_settings"
                        ]["containers"][0]["settings"]["elements"][0]["options"]
                        .get("text")
                        .get("text")
                    )

                    number = self.get_reqid(apartment)
                    id_parts = number.replace("*", "").split(".")

                    if 'class="sc-state available"' not in apartment:
                        continue

                    if number == "2.0.02":
                        url = self.request_url[0 : len(self.request_url) - 1] + "2-0-02"
                    else:
                        url = self.request_url + id_parts[0] + "-" + id_parts[-1]
                    response = requests.get(url)

                    yield {
                        "provider": "amwinterfeldt",
                        "location": self.get_location(apartment),
                        "number": number,
                        "rooms": self.get_rooms(apartment),
                        "size": self.get_size(apartment),
                        "price": self.get_price(response.text),
                        "status": "free",
                        "floor": self.get_floor(apartment),
                    }

    def get_reqid(self, text: str) -> str:
        reqid = ""
        index = text.find("Status")  # TODO checken ob es mehr als 1 "Status" gibt
        while True:
            reqid += text[index]
            index -= 1
            if text[index] == "-" or index <= 0:
                break
        reqid = reqid[::-1].strip().split("<")
        return reqid[0]  # TODO chekcne ob "reqid[0]" existiert

    def get_location(self, text: str) -> str:
        location = ""
        index = text.find("<p>") + 2  # TODO checken ob es mehr als 1 "<p>" gibt
        while text[index] != "-":
            index += 1
            if text[index] == "-":
                break
            location += text[index]
        return location

    def get_rooms(self, text: str) -> str:
        rooms = ""
        index = text.find("m²") + 7  # TODO checken ob es mehr als 1 "m²" gibt
        while True:
            rooms += text[index]
            index += 1
            if text[index].isalpha() or index <= 0:
                break
        return rooms

    def get_size(self, text: str) -> str:
        size = ""
        index = text.find("m²")  # TODO checken ob es mehr als 1 "m²" gibt
        while True:
            if text[index].isdigit() or text[index] == "," or text[index] == ".":
                size += text[index]
            index -= 1
            if text[index] == ">" or index <= 0:
                break
        return size[::-1]

    def get_price(self, text: str) -> str:
        price = ""
        index = text.find("EUR ")  # TODO checken ob es mehr als 1 "EUR" gibt
        while text[index] != ">":
            index -= 1
            if text[index] == ">":
                break
            price += text[index]
        return price[::-1]

    def get_floor(self, text: str) -> str:
        floor = ""
        index = text.find("Etage") - 1  # TODO checken ob es mehr als 1 "Etage" gibt
        while True:
            floor += text[index]
            index -= 1
            if text[index] == "/" or index <= 0:
                break
        return floor
