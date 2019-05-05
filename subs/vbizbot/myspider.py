import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://masothue.vn/tra-cuu-ma-so-thue-theo-loai-hinh-doanh-nghiep/cong-ty-trach-nhiem-huu-han-1-thanh-vien-ngoai-nn-1']

    def parse(self, response):
        for title in response.css('h3'):
            yield {'title': title.css('a ::text').get()}

        for next_page in response.css('a.page-numbers'):
            yield response.follow(next_page, self.parse)
