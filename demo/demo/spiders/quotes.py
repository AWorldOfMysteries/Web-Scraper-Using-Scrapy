# import scrapy
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor

# class MySpider(CrawlSpider):
#         name = "quotes"
#         allowed_domains = ["quotes.toscrape.com"]
#         start_urls = ["https://quotes.toscrape.com/"]

#         rules = (
#             Rule(LinkExtractor(allow="page", deny=["/page/2", "/page/3"])),
#             Rule(LinkExtractor(allow="author"), callback="parse_author")
#             )

#         def parse_author(self, response):
#             yield{
#                 "name" : response.css("div.author-details h3::text").get(),        
#                 "desc" : response.css("div.author-description::text").get()
#             }

import scrapy


class AuthorSpider(scrapy.Spider):
    name = "author"

    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        author_page_links = response.css(".author + a")
        yield from response.follow_all(author_page_links, self.parse_author)

        pagination_links = response.css("li.next a")
        yield from response.follow_all(pagination_links, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default="").strip()

        yield {
            "name": extract_with_css("h3.author-title::text"),
            "birthdate": extract_with_css(".author-born-date::text"),
            "bio": extract_with_css(".author-description::text"),
    }