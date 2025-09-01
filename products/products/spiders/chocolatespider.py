import scrapy


class ChocolatespiderSpider(scrapy.Spider):
    name = "chocolatespider"
    allowed_domains = ["chocolate.co.uk"]
    start_urls = ["https://chocolate.co.uk/collections/all"]

    def parse(self, response):
        products = response.xpath('//product-item[@class="product-item "]')

        for product in products:
            yield {
                'name': product.xpath('.//a[@class="product-item-meta__title"]/text()').get(),
                'price': ''.join(product.xpath('.//span[@class="price"]//text()').getall()).replace('Sale price', '').strip(),
                'link': product.xpath('.//div[@class="product-item-meta"]/a/@href').get()
            }