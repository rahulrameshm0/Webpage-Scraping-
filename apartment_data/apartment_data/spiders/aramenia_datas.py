import scrapy
import random

USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/115.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 Chrome/114.0.0.0 Safari/605.1.15",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Firefox/116.0",
]

class ArameniaDatasSpider(scrapy.Spider):
    name = "aramenia_datas"
    allowed_domains = ["www.list.am"]
    start_urls = ["https://www.list.am/en/category/56"]

    def start_requests(self):

        for url in self.start_urls:

            headers = {
                "User-Agent": random.choice(USER_AGENTS),
                "Accept-Language": "en-US,en;q=0.9",
                "Accept": "text/html,application/xhtml+xml"

            }

            yield scrapy.Request(
                url,
                headers=headers,
                meta={
                    "playwright": True,
                    "playwright_page_coroutines": [
                        ("wait_for_selector", 'div.gl')
                    ],
                },

                callback=self.parse
            )

    def parse(self, response):
        apartment_data = response.xpath('//div[@class="gl"]/a')

        for apartment in apartment_data:

            amount = apartment.xpath('.//div[@class="p"]/text()').get()

            description = apartment.xpath('.//div[@class="l"]/text()').get()

            place = apartment.xpath('.//div[@class="at"]/text()').get()

            yield {

                "Amount": amount,

                "Description": description,

                "Place": place

            }

        # Pagination
        next_page = response.xpath('//div[@class="dlf"]/a[contains(text(), "Next")]/@href').get()

        if next_page:

            yield response.follow(url=next_page,
                                  callback=self.parse,
                                  headers={
                                      "User-Agent": random.choice(USER_AGENTS),
                                      "Accept-Language": "en-US,en;q=0.9",
                                      "Accept": "text/html,application/xhtml+xml"

                                  })


