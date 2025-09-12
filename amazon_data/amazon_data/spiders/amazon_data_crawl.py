import scrapy

class AmazonDataSpider(scrapy.Spider):
    name = "amazon_data_crawl"
    allowed_domains = ["amazon.in"]
    start_urls = ["https://www.amazon.in/s?k=lenovo+laptop"]

    def start_requests(self):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/139.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9",
        }
        for url in self.start_urls:
            yield scrapy.Request(url=url, headers=headers, callback=self.parse)

    def parse(self, response):
        products = response.xpath('//div[@data-component-type="s-search-result"]')
        self.logger.info(f"Found {len(products)} products on this page")

        for idx, product in enumerate(products, start=1):
            title = product.xpath('.//a[contains(@class, "a-link-normal")]/h2[contains(@class, "a-text-normal")]/span/text()').get()
            price = product.xpath('.//span[@class="a-price-whole"]/text()').get()
            m_r_p = product.xpath('.//span[contains(@class, "a-text-price")]/span[@class="a-offscreen"]/text()').get()
            reviews = product.xpath('.//a[contains(@class, "a-link-normal")]/span[contains(@class, "s-underline-text")]/text()').get()
            ratings = product.xpath('.//i[@data-cy="reviews-ratings-slot"]/span[@class="a-icon-alt"]/text()').get()
            link = product.xpath('.//div[@data-cy="title-recipe"]/a[contains(@class, "a-text-normal")]/@href').get()

            # if title and "lenovo" in title.lower():
            if title and "lenovo" in title.lower():
                yield {
                    "title": title,
                    "price": price,
                    "M.R.P": m_r_p,
                    "Reviews": reviews,
                    "Ratings": ratings,
                    "link": link,
                }

        pagination = response.xpath('//span[@aria-label="pagination"]')
        next_page = pagination.xpath('//span[@class="a-list-item"]/a[@role="button"]/@href').get()

        if next_page:
            yield response.follow(url=next_page, callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'})

