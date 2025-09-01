from typing import Iterable, Any

import scrapy


class AudibleSpider(scrapy.Spider):
    name = "audible"
    allowed_domains = ["audible.com"]
    start_urls = ["https://www.audible.in/search"]

    def start_requests(self):
        yield scrapy.Request(url='https://www.audible.com/search/', callback=self.parse,
                       headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'})

    def parse(self, response):
        product_container= response.xpath('//div[@class="adbl-impression-container "]//li[contains(@class, "productListItem")]')

        for product in product_container:
            title = product.xpath('.//h3[contains(@class, "bc-heading")]/a/text()').getall()
            author_name = product.xpath('.//li[contains(@class, "authorLabel")]/span/a/text()').getall()
            length = product.xpath('.//li[contains(@class, "runtimeLabel")]/span/text()').get()

            yield {
                'title': title,
                'author_name':author_name,
                'length': length,
                'User-Agent': response.request.headers['User-Agent']
            }

        pagination = response.xpath('//ul[contains(@class, "pagingElements ")]')
        next_page_url = pagination.xpath('//span[contains(@class, "nextButton")]/a/@href').get()

        if next_page_url:
            yield response.follow(url=next_page_url, callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'})