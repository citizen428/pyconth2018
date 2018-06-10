# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['www.python.org']
    start_urls = ['https://www.python.org/jobs/']

    def parse(self, response):
        pass
