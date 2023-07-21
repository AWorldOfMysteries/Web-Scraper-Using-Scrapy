import scrapy

class BBCSpider(scrapy.Spider):
    name = "bbc"
    allowed_domains = ["www.bbc.com"]
    start_urls = [
        "https://www.bbc.com/hindi/topics/c2lej0594knt?page=1", # Tech
        "https://www.bbc.com/hindi/topics/cwr9j8g1kj9t?page=1", # Sports
        "https://www.bbc.com/hindi/topics/c06gq3n0pp7t?page=1", # Entertainment
        "https://www.bbc.com/hindi/topics/c9wpm0en87xt?page=1", # International
        "https://www.bbc.com/hindi/topics/ckdxnkz7607t?page=1", # India
        "https://www.bbc.com/hindi/topics/c2e4q0z9qznt?page=1", # Social
        "https://www.bbc.com/hindi/topics/cw9kv0kpxydt?page=1", # Videos
    ]

    def parse(self, response):
        
        news_links = response.css("li.bbc-t44f9r a")
        yield from response.follow_all(news_links, self.parse_news)

        next_page = int(response.url[-1]) + 1
        next_page_link = response.url[:-1] + str(next_page)

        if next_page_link is not None:
            self.log(f"Heading to page {next_page}")
            yield scrapy.Request(next_page_link, callback=self.parse)

    def parse_news(self, response):
        yield{
            "Heading" : response.css('h1#content::text').get(default=""),
            "URL" : response.url,
            "Content" : response.css('p[dir="ltr"]::text').getall()
        }