import scrapy
from scrapy_playwright.page import PageMethod

class LaptopsSpider(scrapy.Spider):
    name = "laptops"
    allowed_domains = ["webscraper.io"]
    start_urls = ["https://webscraper.io/test-sites/e-commerce/more/computers/laptops"]

    def start_requests(self):
        yield scrapy.Request(
            url=self.start_urls[0],
            meta=dict(
                playwright=True,
                playwright_page_methods=[
                    # Keep clicking "More" until it's gone
                    PageMethod("evaluate", """
                        async () => {
                            while (true) {
                                const moreBtn = document.querySelector("a.btn.btn-primary.btn-lg.btn-block");
                                if (!moreBtn || moreBtn.style.display === "none") break;
                                moreBtn.click();
                                await new Promise(r => setTimeout(r, 1000)); // wait for new items
                            }
                        }
                    """),
                ],
                errback=self.errback,
            ))

    def parse(self, response):
        laptops_data = response.xpath('//div[contains(@class, "card")]')

        for laptops in laptops_data:
            title = laptops.xpath('.//a[@itemprop="name"]/@title').get()
            amount = laptops.xpath('.//h4[@itemprop="offers"]/text()').get()
            description = laptops.xpath('.//p[@itemprop="description"]/text()').get()
            # rating = laptops.xpath('.//div[@itemprop="aggregateRating"]').get()
            reviews = laptops.xpath('.//span[@itemprop="reviewCount"]/text()').get()

            yield {
                'Title': title,
                'Amount': amount,
                'Description': description,
                # 'Rating': rating,
                'Reviews': reviews,
            }
    async def errback(self, failure):
        self.logger.error(repr(failure))
