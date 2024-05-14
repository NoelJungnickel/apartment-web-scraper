import scrapy
import json
import requests


class Marshall1Spider(scrapy.Spider):
    name = "marshall1"
    allowed_domains = ["marshall1.de"]
    start_urls = ["https://www.marshall1.de/de/portfolio/grundrisse/"]
    url = "https://www.marshall1.de/wp-admin/admin-ajax.php"
    params = {
        "srengine": "6",
    }

    def parse(self, response):
        apartments_list = response.css("rs-layer::text").getall()
        apartments_list_clean = []
        for i in range(len(apartments_list)):
            clean_text = apartments_list[i].replace("\n", "").replace("\t", "").strip()
            if (
                any(c.isdigit() for c in clean_text)
                and len(clean_text) < 10
                and "." in clean_text
                and not clean_text.endswith("OG")
            ):
                apartments_list_clean.append(clean_text)

        data = {
            "action": "revslider_ajax_call_front",
            "client_action": "get_slider_html",
            "usage": "modal",
        }
        for idx in apartments_list_clean:
            print("THIS LINE ------------------------->", idx)
            response = requests.post(
                self.url,
                params=self.params,
                data=data | {"alias": idx.replace(".", "-").replace("*", "")},
            )

            clean_text = (
                response.text.replace("\\t", "").replace("\\n", "").replace("\\", "")
            )

            yield {
                "provider": "marshall1",
                "location": self.get_location(clean_text),
                "number": idx,
                "rooms": self.get_rooms(clean_text),
                "size": self.get_size(clean_text),
                "price": self.get_price(clean_text),
                "status": self.get_status(clean_text),
                "floor": self.get_floor(clean_text),
                # "text": clean_text
            }

    def get_location(self, text: str) -> str:
        location = ""
        index = text.find("Haus") - 1  # TODO checken ob es mehr als 1 "Haus" gibt
        while text[index] != "<":
            index += 1
            if text[index] == "<":
                break
            location += text[index]
        return location

    def get_rooms(self, text: str) -> str:
        rooms = ""
        index = text.find("Room")  # TODO checken ob es mehr als 1 "Room" gibt
        while True:
            if text[index].isdigit():
                rooms += text[index]
            index -= 1
            if text[index] == ">" or index <= 0:
                break
        return rooms[::-1]

    def get_size(self, text: str) -> str:
        size = ""
        index = text.find(
            "living space"
        )  # TODO checken ob es mehr als 1 "living space" gibt
        while True:
            if text[index].isdigit() or text[index] == "," or text[index] == ".":
                size += text[index]
            index -= 1
            if text[index] == ">" or index <= 0:
                break
        return size[::-1]

    def get_price(
        self, text: str
    ) -> str:  # TODO CHECK IF APARTMENT IS AVAILABLE -> IF NOT RETURN NOTHING FOR PRICE
        price = ""
        index = text.find("EUR")  # TODO checken ob es mehr als 1 "EUR" gibt
        while text[index] != ">":
            index -= 1
            if text[index] == ">":
                break
            price += text[index]
        return price[::-1]

    def get_status(self, text: str) -> str:
        status = ""
        index = text.find("sc-state-text") + len(
            "sc-state-text"
        )  # TODO checken ob es mehr als 1 "sc-state-text" gibt
        while True:
            if text[index].isalpha():
                status += text[index]
            index += 1
            if text[index] == ">" or index <= 0:
                break
        return status

    def get_floor(self, text: str) -> str:
        floor = ""
        index = text.find("Room") + len(
            "Room"
        )  # TODO checken ob es mehr als 1 "Room" gibt
        while True:
            if text[index].isalpha():
                floor += text[index]
            index += 1
            if text[index] == "<" or index <= 0:
                break
        return floor
