import scrapy


class apSpider(scrapy.Spider):
    name = "ap"
    start_urls = [
        'https://apnews.com/hub/ap-top-news'
    ]

    def parse(self, response):
        for article in response.css('div.FeedCard'):
            yield {
                'title': article.css('h1.Component-h1-0-2-111::text').get(),
                'author': article.css('span.Component-bylines-0-2-113::text').get(),
                'date': article.css('span.Timestamp::text').get(),
                'content': article.css('p::text').get()
            }