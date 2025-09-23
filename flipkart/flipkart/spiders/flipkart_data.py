from typing import Iterable, Any

import scrapy



class FlipkartDataSpider(scrapy.Spider):
    name = "flipkart_data"
    allowed_domains = ["www.flipkart.com"]
    start_urls = ["https://www.flipkart.com/computers/monitors/pr?sid=6bo,9no&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_799320d2-eddf-4a36-8fd3-ef850d6f0ef4_1_X1NCR146KC29_MC.VAJ1HQDC38FS&otracker=hp_rich_navigation_3_1.navigationCard.RICH_NAVIGATION_Electronics~Computer%2BPeripherals~Monitors_VAJ1HQDC38FS&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&cid=VAJ1HQDC38FS"]

    def start_requests(self):
        headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.9"
        }

        for url in self.start_urls:
            yield scrapy.Request(url=url,headers=headers, callback=self.parse)

    def parse(self, response):
        product_data = response.xpath('//div[@data-id]')

        for product in product_data:
            title = product.xpath('string(.//div[@class="KzDlHZ"])').get()
            rating = product.xpath('.//div[@class="XQDdHH"]/text()').get()
            review_count = product.xpath('.//span[contains(text(), "Reviews")]/text()').get()
            if review_count:
                review_count = review_count.replace('\xa0', '').strip()
            rating_count = product.xpath('.//span[contains(text(), "Ratings")]/text()').get()
            if rating_count:
                rating_count = rating_count.replace('\xa0', '').strip()
            current_amount = product.xpath('.//div[@class="Nx9bqj _4b5DiR"]/text()').get()
            m_r_p = product.xpath('.//div[contains(@class, "yRaY8j")]/text()').getall()
            percentage = product.xpath('.//div[@class="UkUFwK"]/span/text()').get()

            yield {
                "Title": title,
                "Rating": rating,
                "Review": review_count,
                "Rating_count": rating_count,
                "Current Amount": current_amount,
                "M.R.P": m_r_p,
                "Percentage": percentage
            }
        pagination = response.xpath('//nav[@class="WSL9JP"]')
        next_page = pagination.xpath('//a[span[text()="Next"]]/@href').get()


        if next_page:
            yield response.follow(url=next_page, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'})
