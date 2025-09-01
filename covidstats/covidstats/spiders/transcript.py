from typing import Iterable, Any

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class TranscriptSpider(CrawlSpider):
    name = "transcript"
    allowed_domains = ["subslikescript.com"]
    # start_urls = ["https://subslikescript.com/series_letter-X"]

    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'

    def start_requests(self):
        yield scrapy.Request(url='https://subslikescript.com/series_letter-X', headers={'user-agent':self.user_agent})

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//ul[@class="scripts-list"]/li/a')), callback="parse_item", follow=True, process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths=('(//a[@rel="next"])[1]'))),
    )

    def set_user_agent(self, request, spider):
        request.headers['User-Agent'] = self.user_agent
        return request

    def parse_item(self, response):
        article = response.xpath("//article[@class='main-article']")

        yield {
                'title': article.xpath('./h1/text()').get(),
                'plot': article.xpath('./p/text()').get(),
               # 'transcript': article.xpath("./div[@class='full-script']/text()").get(),
                'url': response.url,
                'user-agent': response.request.headers['User-Agent']
           }
