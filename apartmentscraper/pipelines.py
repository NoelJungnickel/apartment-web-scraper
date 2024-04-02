from itemadapter import ItemAdapter
import pandas


class ApartmentscraperPipeline:

    items = []

    slots = [
        "Location in the object",
        "Apartment number",
        "Room",
        "Living space (in m²)",
        "Total purchase price",
        "Status",
    ]

    def close_spider(self, spider):
        df = pandas.DataFrame(list(item["apartment"] for item in self.items), columns = self.slots, index=list(range(1, len(self.items) + 1)))
        df.to_excel("apartments.xlsx")

    def process_item(self, item, spider):

        if len(item["apartment"]) < 2:
            return
        
        item["apartment"] = item["apartment"][1:]

        item["apartment"][3] = item["apartment"][3].replace(",", ".")
        item["apartment"][4] = item["apartment"][4].replace(" ", "").replace("€", " €").replace(",", ".")


        self.items.append(item)

        return item