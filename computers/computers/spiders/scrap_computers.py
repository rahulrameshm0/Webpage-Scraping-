import scrapy


class ScrapComputersSpider(scrapy.Spider):
    name = "scrap_computers"
    allowed_domains = ["webscraper.io"]
    start_urls = ["https://webscraper.io/test-sites/e-commerce/static/computers/laptops"]

    def parse(self, response):
        computers_data = response.xpath('//div[@class="col-md-4 col-xl-4 col-lg-4"]')

        for computers in computers_data:
            name = computers.xpath('.//h4/a[@itemprop="name"]/@title/text()').get()
            price = computers.xpath('.//h4/span[@itemprop="price"]/text()').get()
            description = computers.xpath('.//p[@itemprop="description"]/text()').get()
            rating = computers.xpath('.//p[@data-rating]/@data-rating').get()
            review = computers.xpath('.//span[@itemprop="reviewCount"]/text()').get()

            yield {
                'Name': name,
                'Price': price,
                'Description': description,
                'Rating': rating,
                'review': review,
            }

        pagination = response.xpath('//ul[@class="pagination"]')
        nex_page = pagination.xpath('.//a[@rel="next"]/@href').get()

        if nex_page:
            yield response.follow(nex_page, callback=self.parse)

