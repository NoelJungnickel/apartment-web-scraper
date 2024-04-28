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

    """def close_spider(self, spider):
        df = pandas.DataFrame(self.items)
        df.set_index('location', inplace=True)
        df.to_excel("apartments.xlsx")

    def process_item(self, item, spider):
        item["size"] = item["size"].replace(",", ".")
        item["price"] = item["price"].replace(" ", "").replace("€", " €").replace(",", ".")

        self.items.append(item)

        return item"""