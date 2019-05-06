import random
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import requests


#scrapy runspider myspider.py
class MySpider(scrapy.Spider):
    name = 'blogspider'
    DOWNLOADER_MIDDLEWARES = {
        'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 1
    }
    download_delay = 0.5
    proxy_pool = [
        '36.67.199.89:30625', '52.68.127.244:80',
        '140.227.73.118:3128'
    ]
    # post_url = 'http://localhost:5000/api/vbiz'

    post_url = 'https://vbiz.vnappmob.com/api/vbiz'

    def start_requests(self):
        print('------->start_requests--->')
        urls = [
            'https://masothue.vn/tra-cuu-ma-so-thue-theo-loai-hinh-doanh-nghiep/cong-ty-trach-nhiem-huu-han-1-thanh-vien-ngoai-nn-1',
        ]
        for url in urls:
            request = scrapy.Request(
                url=url,
                callback=self.parse,
                meta={'proxy': random.choice(self.proxy_pool)})
            yield request

    def parse(self, response):

        for href in response.css('.tax-listing').xpath(
                '//h3/a/@href').getall():
            # print(href)
            yield response.follow(
                href,
                self.parse_biz,
                meta={'proxy': random.choice(self.proxy_pool)})

        for href in response.css('ul.page-numbers li a::attr(href)'):
            # print(href)
            yield response.follow(
                href,
                self.parse,
                meta={'proxy': random.choice(self.proxy_pool)})

    def parse_biz(self, response):
        taxinfo = response.css('.table-taxinfo')

        vbiz_name = taxinfo.xpath(
            '//th[contains(@itemprop, "name")]/text()').get()
        vbiz_code = taxinfo.xpath(
            '//td[contains(@itemprop, "taxID")]/text()').get()
        address = taxinfo.xpath(
            '//td[contains(@itemprop, "address")]/text()').get()
        vbiz_address = address.replace('Vietnam', 'Việt Nam')
        vbiz_phone = taxinfo.xpath(
            '//td[contains(@itemprop, "telephone")]/text()').get()
        alltaxtd = taxinfo.xpath('//td/text()').getall()
        vbiz_register_date = None
        for item in alltaxtd:
            if validate_date(item):
                from dateutil import parser
                vbiz_register_date = parser.parse(item, dayfirst=False)

        manganh = response.css('.table').xpath('//strong/a/text()').get()

        post_data = {
            "vbiz_address": vbiz_address,
            "vbiz_category_id": manganh,
            "vbiz_code": vbiz_code,
            "vbiz_email": '',
            "vbiz_name": vbiz_name,
            "vbiz_phone": vbiz_phone if vbiz_phone is not None else '',
            "vbiz_region_id": 0,
            "vbiz_register_date": vbiz_register_date.strftime('%d/%m/%Y')
        }

        print(post_data)
        post_vbiz(self.post_url, post_data)


def post_vbiz(post_url, post_data):
    """post_vbiz"""
    response = requests.post(post_url, json=post_data)
    print(response.status_code)


def validate_date(date_text):
    """validate_date"""
    from dateutil import parser

    try:
        parser.parse(date_text)
        return True
    except:  #pylint: disable=W
        return False
