# -*- coding: utf-8 -*-
import scrapy


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
            yield {
                "title": job.css('.listing-company-name > a::text').extract_first(),
                "company": job.css('.listing-company-name::text').extract(),
                "location": job.css('.listing-location > a::text').extract_first(),
                "tags": job.css('.listing-job-type > a::text').extract(),
                "date": job.css('.listing-posted > time::text').extract_first()
            }
