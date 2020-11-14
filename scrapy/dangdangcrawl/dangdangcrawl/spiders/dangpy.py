import scrapy
from dangdangcrawl.items import DangdangcrawlItem
from scrapy.http import Request as scrapyReq
class DangpySpider(scrapy.Spider):
    name = 'dangpy'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=python&act=input&page_index=']

    def parse(self, response):
        item=DangdangcrawlItem()
        item['title']= response.xpath("//a[@name='itemlist-title']/@title ").extract()
        item['comment'] = response.xpath("//a[@name='itemlist-review']/text() ").extract()
        item['price'] = response.xpath("//span[@class='search_pre_price']/text() ").extract()
        item['link'] = response.xpath("//a[@name='itemlist-title']/@href ").extract()
        yield item
        for i in range(2,3):
            this_url = self.start_urls[0]+str(i)
            print (this_url)
            yield scrapyReq(this_url,callback=self.parse)
