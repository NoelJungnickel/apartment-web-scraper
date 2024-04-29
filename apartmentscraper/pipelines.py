from itemadapter import ItemAdapter
import pandas


class ApartmentscraperPipeline:

    items = []

    """def close_spider(self, spider):
        df = pandas.DataFrame(self.items)
        df.set_index("provider", inplace=True)
        df.to_excel("apartments.xlsx")

    def process_item(self, item, spider):
        item["size"] = item["size"].replace(",", ".") + " m²"
        item["price"] = item["price"].replace(" ", "").replace("€", " €").replace(",", ".")

        self.items.append(item)

        return item"""