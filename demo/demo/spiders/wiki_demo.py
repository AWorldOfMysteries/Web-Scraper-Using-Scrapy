# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
import urllib


class OurfirstbotSpider(scrapy.Spider):
    name = 'ourfirstbot'
    start_urls = [
        'https://en.wikipedia.org/wiki/List_of_common_misconceptions',
    ]

    def parse(self, response):
        #yield response
        headings = response.css('.mw-headline').extract()       
        datas = response.css('ul').extract()       

        
        for item in zip(headings, datas):
            all_items = {
                'headings' : BeautifulSoup(item[0]).text,
                'datas' : BeautifulSoup(item[1]).text,


            }


            yield all_items