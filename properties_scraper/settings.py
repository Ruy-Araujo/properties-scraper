# Scrapy settings for properties_scraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "properties_scraper"

SPIDER_MODULES = ["properties_scraper.spiders"]
NEWSPIDER_MODULE = "properties_scraper.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = "properties_scraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 60/10.0
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
CONCURRENT_REQUESTS_PER_IP = 10

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

URLLENGTH_LIMIT = 5000

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "x-domain": "www.zapimoveis.com.br"
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "properties_scraper.middlewares.PropertiesScraperSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    "properties_scraper.middlewares.PropertiesScraperDownloaderMiddleware": 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    "properties_scraper.pipelines.PropertiesScraperPipeline": 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.epollreactor.EPollReactor"
FEED_EXPORT_ENCODING = "utf-8"
FEED_FORMAT = "json"
FEED_EXPORTERS = {"json": "scrapy.exporters.JsonItemExporter"}

# Search parameters
BUSSINESS = "RENTAL"
LISTINGTYPE = "USED"
UNITTYPES = "APARTMENT,APARTMENT,APARTMENT,HOME,HOME,HOME,HOME,APARTMENT,APARTMENT,APARTMENT,ALLOTMENT_LAND,FARM"
UNITSUBTYPES = "UnitSubType_NONE,DUPLEX,TRIPLEX|STUDIO|KITNET|UnitSubType_NONE,SINGLE_STOREY_HOUSE,KITNET|TWO_STORY_HOUSE|CONDOMINIUM|VILLAGE_HOUSE|PENTHOUSE|FLAT|LOFT|UnitSubType_NONE,CONDOMINIUM,VILLAGE_HOUSE|UnitSubType_NONE,CONDOMINIUM"
USAGETYPES = "RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL,RESIDENTIAL"
UNITTYPESV3 = "APARTMENT,UnitType_NONE,KITNET,HOME,TWO_STORY_HOUSE,CONDOMINIUM,VILLAGE_HOUSE,PENTHOUSE,FLAT,LOFT,RESIDENTIAL_ALLOTMENT_LAND,FARM"
ADDRESCITY = "Belo Horizonte"
