import scrapy
from scrapy.exceptions import CloseSpider
from scrapy.loader import ItemLoader
from properties_scraper.items.property_item import PropertyInfoItem

from urllib.parse import urlencode
from datetime import datetime


class PropertiesSpider(scrapy.Spider):
    name = "properties_spider"
    url = "https://glue-api.zapimoveis.com.br/v2/listings?"

    def start_requests(self):
        self.params = {
            "categoryPage": "RESULT",
            "includeFields": "search(result(listings(listing(listingsCount,sourceId,displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,stamps,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status,priceSuggestion,contractType),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId,createdDate,minisite,tier),medias,accountLink,link)),totalCount),page,facets,fullUriFragments,superPremium(search(result(listings(listing(listingsCount,sourceId,displayAddressType,amenities,usableAreas,constructionStatus,listingType,description,title,stamps,createdAt,floors,unitTypes,nonActivationReason,providerId,propertyType,unitSubTypes,unitsOnTheFloor,legacyId,id,portal,unitFloor,parkingSpaces,updatedAt,address,suites,publicationType,externalId,bathrooms,usageTypes,totalAreas,advertiserId,advertiserContact,whatsappNumber,bedrooms,acceptExchange,pricingInfos,showPrice,resale,buildings,capacityLimit,status,priceSuggestion,contractType),account(id,name,logoUrl,licenseNumber,showAddress,legacyVivarealId,legacyZapId,createdDate,minisite,tier),medias,accountLink,link)),totalCount))",
            "size": 100,
            "from": 7800,
            "listingType": self.settings.get("LISTINGTYPE"),
            "business": self.settings.get("BUSSINESS"),
            "unitTypes": self.settings.get("UNITTYPES"),
            "unitSubTypes": self.settings.get("UNITSUBTYPES"),
            "usageTypes": self.settings.get("USAGETYPES"),
            "unitTypesV3": self.settings.get("UNITTYPESV3"),
            "addressCity": self.settings.get("ADDRESCITY")
        }

        yield scrapy.Request(url=self.url+urlencode(self.params), callback=self.parse)

    def parse(self, response):
        json_response = response.json()

        if self.params["from"] > json_response["page"]["uriPagination"]["totalListingCounter"]:
            raise CloseSpider("No results scrapy stoped...")

        for property in json_response["search"]["result"]["listings"]:
            item = ItemLoader(item=PropertyInfoItem())
            item.add_value("data", property)
            item.add_value("_extract_date", datetime.now().isoformat())
            yield item.load_item()

        self.params.update({"from": self.params["from"] + self.params["size"]})
        yield response.follow(url=self.url + urlencode(self.params), callback=self.parse)
