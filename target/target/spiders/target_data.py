import scrapy


class TargetSpider(scrapy.Spider):
    name = "target_data"
    allowed_domains = ["redsky.target.com"]

    def start_requests(self):
        url = "https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v2"

        params = {
            "key": "9f36aeafbe60771e321a7cc95a78140772ab3e96",
            "channel": "WEB",
            "count": "24",
            "default_purchasability_filter": "true",
            "include_dmc_dmr": "true",
            "include_sponsored": "true",
            "include_review_summarization": "true",
            "keyword": "smart tv",
            "new_search": "true",
            "offset": "0",
            "page": "/s/smart tv",
            "platform": "desktop",
            "pricing_store_id": "1945",
            "spellcheck": "true",
            "store_ids": "1945,1943,1944,2448,905",
            "visitor_id": "01992E73AB3A0201903F60293D77D096",
            "zip": "67062",
        }
        headers = {
            "accept": "application/json",
            "accept-language": "en-GB,en-US;q=0.9,en;q=0.8,la;q=0.7",
            "origin": "https://www.target.com",
            "referer": "https://www.target.com/s?searchTerm=smart+tv",
            "sec-ch-ua": '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                          "AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/139.0.0.0 Safari/537.36",
        }

        yield scrapy.Request(
            url=url,
            headers=headers,
            method="GET",
            cb_kwargs={"params": params},
            callback=self.parse,
        )

    def parse(self, response, params):
        data = response.json()
        # Example: Extract product titles
        products = data.get("data", {}).get("search", {}).get("products", [])
        for product in products:
            yield {
                "title": product.get("item", {}).get("product_description", {}).get("title"),
                "price": product.get("price", {}).get("formatted_current_price"),
                "rating": product.get("ratings_and_reviews", {}).get("statistics", {}).get("rating", {}).get("average"),
            }
