


# class AuthorSpider(scrapy.Spider):
#     name = "author"

#     start_urls = ["https://quotes.toscrape.com/"]

#     def parse(self, response):
#         author_page_links = response.css(".author + a")
#         yield from response.follow_all(author_page_links, self.parse_author)

#         pagination_links = response.css("li.next a")
#         yield from response.follow_all(pagination_links, self.parse)

#     def parse_author(self, response):
#         def extract_with_css(query):
#             return response.css(query).get(default="").strip()

#         yield {
#             "name": extract_with_css("h3.author-title::text"),
#             "birthdate": extract_with_css(".author-born-date::text"),
#             "bio": extract_with_css(".author-description::text"),
#         }







import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import re
from bs4 import BeautifulSoup

## Create an accurate link follower
class NewsonairSpider(CrawlSpider):
    name = "newsonair"
    start_urls = [
        "https://newsonair.gov.in/hindi/Hindi-Default.aspx",
        "https://newsonair.gov.in/hindi/National-Hindi-News.aspx",
        "https://newsonair.gov.in/hindi/International-Hindi-News.aspx",

        "https://newsonair.gov.in/hindi/State-Hindi-News.aspx",
        "https://newsonair.gov.in/hindi/bihar.aspx",
        "https://newsonair.gov.in/hindi/Uttar-Pradesh.aspx",
        "https://newsonair.gov.in/hindi/Madhya-Pradesh.aspx",
        "https://newsonair.gov.in/hindi/Jharkhand.aspx",
        "https://newsonair.gov.in/hindi/Uttarakhand.aspx",
        "https://newsonair.gov.in/hindi/Chhattisgarh.aspx",
        "https://newsonair.gov.in/hindi/Himachal-Pradesh.aspx",

        "https://newsonair.gov.in/hindi/Business-Hindi-News.aspx",
        "https://newsonair.gov.in/hindi/Sports-Hindi-News.aspx"
        ]
    allowed_domains = ["newsonair.gov.in"]

    rules = (
        Rule(LinkExtractor(allow=r'hindi'), callback="parse_news", follow=True),
        # Rule(LinkExtractor(allow=))
    )
    #def parse_content(self, response):

## Design an html parser to filter the hindi text out

    def parse_news(self, response):
        # news = response.css('td[colspan="2"]')
        soup = BeautifulSoup(response.body, 'lxml')
        text = ""
        for para in soup.find_all('p'):
            text = text + para.text
        yield{
            "Headline" : response.css('td[colspan="2"] h2::text').get(default=""),
            "URL" : response.url,
            "Category" : response.css('div.inner-title h3 span::text').get(default=""),
            "Content" : text
        }
