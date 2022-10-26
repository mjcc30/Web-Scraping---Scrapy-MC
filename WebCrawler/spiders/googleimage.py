import scrapy


class GoogleimageSpider(scrapy.Spider):
    name = 'googleimage'
    allowed_domains = ['www.google.com']
    start_urls = ['http://www.google.com/']

    def parse(self, response):
        pass
