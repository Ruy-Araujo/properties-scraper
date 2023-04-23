from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from twisted.internet import task

from datetime import datetime
from properties_scraper.spiders.properties_spider import PropertiesSpider


settings = get_project_settings()
settings.update({"FEED_URI": f"data/{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"})

process = CrawlerProcess(settings)
process.crawl(PropertiesSpider)
process.start()
