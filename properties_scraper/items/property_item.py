from scrapy.item import Item, Field
from itemloaders.processors import TakeFirst


class PropertyInfoItem(Item):
    data = Field(output_processor=TakeFirst())
    _extract_date = Field(output_processor=TakeFirst())
