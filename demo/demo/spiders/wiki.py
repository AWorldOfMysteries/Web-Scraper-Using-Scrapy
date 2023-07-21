import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

import re
from bs4 import BeautifulSoup

class wikiSpider(CrawlSpider):
        name = "wiki"
        allowed_domains = ["hi.wikipedia.org"]
        start_urls = [
              # main page
              "https://hi.wikipedia.org/wiki/%E0%A4%AE%E0%A5%81%E0%A4%96%E0%A4%AA%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A0",
            #   # samaajshastra
            #   "https://hi.wikipedia.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%87%E0%A4%A3%E0%A5%80:%E0%A4%B8%E0%A4%AE%E0%A4%BE%E0%A4%9C%E0%A4%B6%E0%A4%BE%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%8D%E0%A4%B0",
            #   # darshan
            #   "https://hi.wikipedia.org/wiki/%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%87%E0%A4%A3%E0%A5%80:%E0%A4%A6%E0%A4%B0%E0%A5%8D%E0%A4%B6%E0%A4%A8"
              
            #   "",
            #   "",
            #   "",
        ]

        rules = (
            Rule(LinkExtractor(allow=r'%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%87%E0%A4%A3%E0%A5%80'), follow=True),
            Rule(LinkExtractor(deny=(re.compile(r'%E0%A4%B6%E0%A5%8D%E0%A4%B0%E0%A5%87%E0%A4%A3%E0%A5%80*'), re.compile(r'%E0%A4%B5%E0%A4%BF%E0%A4%B6%E0%A5%87%E0%A4%B7'))), callback='parse_page', follow=True)
            )

        def parse_page(self, response):
            soup = BeautifulSoup(response.body, 'lxml')
            text = ""
            for para in soup.find_all('p'):
                text = text + para.text
            yield{
                "Heading" : response.css('span.mw-page-title-main::text').get(default=""),
                "URL" : response.url,
                "Content" : text
            }