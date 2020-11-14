import scrapy
from ali_first.items import AliFirstItem


class FirstSpider(scrapy.Spider):
    name = 'first'
    allowed_domains = ['aliwx.com.cn']
    start_urls = ['https://www.aliwx.com.cn/']

    def parse(self, response):
        item=AliFirstItem()
        item["title"]=response.xpath("//p[@class='title']/text()").extract()
        yield item
