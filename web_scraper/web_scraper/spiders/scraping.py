import scrapy

class ScrapingSpider(scrapy.Spider):
    name = "scraping"
    allowed_domains = ["webscraper.io"]
    start_urls = ["https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"]

    def parse(self, response):
        product_container = response.xpath('//div[@class="col-md-4 col-xl-4 col-lg-4"]')

        for product in product_container:
            name = product.xpath('.//h4/a[@class="title"]/@title').get()
            price = product.xpath('.//span[@itemprop="price"]/text()').get()
            rating = product.xpath('.//p[@data-rating]/@data-rating').get()
            review_count = product.xpath('.//span[@itemprop="reviewCount"]/text()').get()

            yield {
                'name': name.strip(),
                'price': price.strip(),
                'rating': rating,
                'reviews': review_count.strip(),
            }
