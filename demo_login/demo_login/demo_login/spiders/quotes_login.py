# -*- coding: utf-8 -*-
import scrapy
from scrapy import FormRequest
import logging


class QuotesLoginSpider(scrapy.Spider):
    name = 'quotes_login'
    allowed_domains = ['linkedin.com']
    start_urls = ['https://linkedin.com/login']

    def parse(self, response):
        # csrf_toke=response.
        headers= {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        yield FormRequest(url=self.start_urls[0],
                                         formdata={
                                        'txtEmail': 'shirsangshudutta@gmail.com',
                                        'txtPassword': 'times82!'
                                                   },
                                         callback=self.after_login,
                                         headers=headers)
 
    def after_login(self, response):
        # if response.xpath("//a[@href='/logout']/text()").get():
        name=response.xpath("//*[@id='ember106']/div[2]").extract()
        # self.log(name,logging.WARN)
        logging.warning("This is a warning")



