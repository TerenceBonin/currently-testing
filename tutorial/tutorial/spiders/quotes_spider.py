import scrapy
from scrapy_splash import SplashRequest

class SpiderTest(scrapy.Spider):
    name = "quotes"
    def start_request(self):
        url = "https://www.leboncoin.fr/voitures/offres/pays_de_la_loire"
        yield SplashRequest(url)

    def parse(self, response):
        products_selector = response.css('[data-qa-id="aditem_container"]')
        for product in products_selector:
            yield {
                'name': product.css('p[title]::attr(title)').get()
            }