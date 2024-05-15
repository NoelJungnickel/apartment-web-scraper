from itemadapter import ItemAdapter
import pandas


class ApartmentscraperPipeline:

    items = []

    def close_spider(self, spider):
        df = pandas.DataFrame(self.items)
        df.set_index("provider", inplace=True)
        df.to_excel("apartments.xlsx")

    def process_item(self, item, spider):
        item["location"] = item["location"].strip()
        item["number"] = item["number"].strip()
        item["rooms"] = item["rooms"].strip()
        item["size"] = item["size"].strip()
        item["price"] = item["price"].replace("€", "").strip()
        item["status"] = item["status"].strip()
        item["floor"] = item["floor"].strip()

        item["size"] = item["size"] + " m²"
        item["price"] = item["price"].replace(",", ".") + " €"
        item["status"] = (
            item["status"].replace("notavailable", "sold").replace("available", "free")
        )
        if item["floor"] == "p":
            item["floor"] = "EG"

        self.items.append(item)

        return item
