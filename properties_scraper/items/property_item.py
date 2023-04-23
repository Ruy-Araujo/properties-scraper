from scrapy.item import Item, Field
from itemloaders.processors import TakeFirst


class PropertyInfoItem(Item):
    data = Field(output_processor=TakeFirst())
    _extract_date = Field(output_processor=TakeFirst())


def __repr__(self):
    return repr({"property_id": self["data"]["listing"]["id"]})


def __str__(self):
    return f'Extracted property: {self["data"]["listing"]["id"]}'
