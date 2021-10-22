from fastapi import FastAPI
from timeit import default_timer as timer
import scrapy
from scrapy_splash import SplashRequest

class SpiderTest(scrapy.Spider):
    name = "Spooder"
    def start_request(self):
        url = "https://www.youtube.com/"
        yield SplashRequest(url)

    def parse(self, response):
        products_selector = response.css('[data-qa-id="aditem_container"]')
        for product in products_selector:
            yield {
                'name': product.css('p[title]::attr(title)').get()
            }


# uvicorn main:app --reload

# app = FastAPI()

# @app.get("/")
# async def root():
#     return "hello man"

# @app.get("/op")
# async def add(a: int=0, b: int=0):
#     start_time = timer()
#     operations = {"a+b": a + b, "b-a": b - a,"b/a": b / a}
#     exec_time = timer() - start_time
#     return {"a" : a, "b" : b , "operations": operations, "exec_time": exec_time}