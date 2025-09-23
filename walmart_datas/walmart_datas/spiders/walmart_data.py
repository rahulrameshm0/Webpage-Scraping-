import scrapy

class WalmartDataSpider(scrapy.Spider):
    name = "walmart_data"
    allowed_domains = ["www.walmart.com"]
    start_urls = ["https://www.walmart.com/search/?cat_id=0&facet=retailer%3AWalmart.com&query=Samsung+phone"]

    def parse(self, response):
        product_container = response.xpath('//div[contains(@class,  "b--near-white")]')

        for product in product_container:
            pass
