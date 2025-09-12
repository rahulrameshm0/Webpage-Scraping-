# import scrapy
# import json
# from scrapy_playwright.page import PageMethod
#
# class LaptopsSpider(scrapy.Spider):
#     name = "laptops"
#     allowed_domains = ["webscraper.io"]
#     start_urls = ["https://webscraper.io/test-sites/e-commerce/ajax/computers/laptops"]
#
#     def parse(self, response):
#         laptops_data = response.xpath('//div[contains(@class, "row ecomerce-items ecomerce-items-ajax")]/@data-items').get()
#
#         if laptops_data:
#             products = json.loads(laptops_data)
#
#             review_counts = response.xpath('//span[@itemprop="reviewCount"]/text()').getall()
#         for laptops in products:
#             title = laptops.get("name")
#             amount = laptops.get("price")
#             description = laptops.get("description")
#             # rating = laptops.xpath('.//div[@itemprop="aggregateRating"]').get()
#
#             encoded_title = laptops.get("title")
#             reviews = None
#             if encoded_title:
#                 try:
#                     reviews = round(int(encoded_title, 36)) % 15
#                 except ValueError:
#                     reviews = None
#
#             yield {
#                 'Title': title,
#                 'Amount': amount,
#                 'Description': description,
#                 # 'Rating': rating,
#                 'Reviews': reviews,
#             }


import scrapy
import json


class LaptopsSpider(scrapy.Spider):
    name = "laptops"
    allowed_domains = ["webscraper.io"]
    start_urls = ["https://webscraper.io/test-sites/e-commerce/ajax/computers/laptops"]

    def parse(self, response):
        laptops_data = response.xpath(
            '//div[contains(@class, "row ecomerce-items ecomerce-items-ajax")]/@data-items'
        ).get()

        if laptops_data:
            products = json.loads(laptops_data)

            for product in products:
                print(product)
                name = product.get("title")          # readable product name
                price = product.get("price")
                description = product.get("description")
                reviews = product.get("reviews")

                yield {
                    "Title": name,
                    "Amount": price,
                    "Description": description,
                    "Reviews": reviews,
                }
                break
