import scrapy


class NewSpider(scrapy.Spider):
    name = "new_spider"
    start_urls = ['https://192.168.230.130/photography/']

    def parse(self, response):
        for picture in response.css('img'):
            yield{
                'Image Link': picture.xpath('@src').extract_first(),
            }
        page_selector = '.next a ::attr(href)'
        next_page = response.css(page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
