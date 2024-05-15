from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from apartmentscraper.spiders.amwinterfeldt import AmwinterfeldtSpider
from apartmentscraper.spiders.ba94 import Ba94Spider
from apartmentscraper.spiders.franz import FranzSpider
from apartmentscraper.spiders.kurfuerst import KurfuerstSpider
from apartmentscraper.spiders.marshall1 import Marshall1Spider


def main():
    settings = get_project_settings()
    process = CrawlerProcess(settings)

    process.crawl(AmwinterfeldtSpider)
    process.crawl(Ba94Spider)
    process.crawl(FranzSpider)
    process.crawl(KurfuerstSpider)
    process.crawl(Marshall1Spider)
    process.start()


if __name__ == "__main__":
    main()
