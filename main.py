from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from scrapy.utils.reactor import install_reactor
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor, defer

from apartmentscraper.spiders.amwinterfeldt import AmwinterfeldtSpider
from apartmentscraper.spiders.ba94 import Ba94Spider
from apartmentscraper.spiders.franz import FranzSpider
from apartmentscraper.spiders.kurfuerst import KurfuerstSpider
from apartmentscraper.spiders.marshall1 import Marshall1Spider


def main():
    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)

    @defer.inlineCallbacks
    def crawl():
        yield runner.crawl(AmwinterfeldtSpider)
        yield runner.crawl(Ba94Spider)
        yield runner.crawl(FranzSpider)
        yield runner.crawl(KurfuerstSpider)
        yield runner.crawl(Marshall1Spider)
        reactor.stop()

    crawl()
    reactor.run()


if __name__ == "__main__":
    main()
