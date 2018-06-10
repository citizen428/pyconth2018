# -*- coding: utf-8 -*-
import scrapy

from pyconth.items import Job
from scrapy.loader import ItemLoader


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['www.python.org']
    start_urls = ['https://www.python.org/jobs/']

    # Find job pages
    def parse(self, response):
        for jobs in response.css('.pagination a[href^="?page"]::attr(href)').extract():
            page = response.urljoin(jobs)
            yield scrapy.Request(page, callback=self.parse_jobs)

    # Extract jobs from job pages
    def parse_jobs(self, response):
        for job in response.css('.list-recent-jobs > li'):
            loader = ItemLoader(item=Job(), selector=job)
            loader.add_css('title', '.listing-company-name > a::text')
            loader.add_css('company', '.listing-company-name::text')
            loader.add_css('location', '.listing-location > a::text')
            loader.add_css('tags', '.listing-job-type > a::text')
            loader.add_css('date', '.listing-posted > time::text')
            yield loader.load_item()
