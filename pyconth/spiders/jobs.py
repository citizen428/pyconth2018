# -*- coding: utf-8 -*-
import scrapy

from pyconth.items import Job, JobLoader
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class JobsSpider(CrawlSpider):
    name = 'jobs'
    allowed_domains = ['www.python.org']
    start_urls = ['https://www.python.org/jobs/']

    rules = [
        Rule(
            LinkExtractor(allow=r'\?page='),
            callback='parse_jobs'
        )
    ]

    # Extract jobs from job pages
    def parse_jobs(self, response):
        for job in response.css('.list-recent-jobs > li'):
            loader = JobLoader(selector=job)
            loader.add_css('title', '.listing-company-name > a::text')
            loader.add_css('company', '.listing-company-name::text')
            loader.add_css('location', '.listing-location > a::text')
            loader.add_css('tags', '.listing-job-type > a::text')
            loader.add_css('date', '.listing-posted > time::text')
            yield loader.load_item()
