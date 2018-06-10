# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy.loader.processors import Identity, Join, MapCompose, TakeFirst


def tagify(s):
    return s.lower().replace(' ', '_')


class Job(scrapy.Item):
    title = scrapy.Field()
    company = scrapy.Field()
    location = scrapy.Field()
    tags = scrapy.Field()
    date = scrapy.Field()


class JobLoader(scrapy.loader.ItemLoader):
    default_item_class = Job
    default_output_processor = TakeFirst()

    company_in = MapCompose(lambda s: s.strip())
    company_out = Join('')
    tags_out = MapCompose(tagify)
