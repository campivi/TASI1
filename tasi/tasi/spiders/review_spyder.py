from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from tasi.items import androidCentralItem
import re


class review_spyder(Spider):
    name = "androidcentral"
    allowed_domains = ["androidcentral.com"]
    start_urls = [
        "http://www.androidcentral.com/search/xperia%20xz?query=xperia%20xz"]

    def parse(self, response):
        links = response.xpath(
            '//*[@id="grid_items"]/div/div/h2/a/@href').extract()
        print("Links:", links)
        # We stored already crawled links in this list
        crawledLinks = []
        linkPattern = re.compile("^http://www.androidcentral.com/+")
        for link in links:
            # If it is a proper link and is not checked yet, yield it to the
            # Spider
            if (linkPattern.match(link)) and (link not in crawledLinks):
                #link = "http://www.androidcentral.com" + link
                crawledLinks.append(link)
                yield Request(link, self.parse_page)

    def parse_page(self, response):
        title = response.xpath(
            '//*[@id="article-header"]/section/div/div/section/h1/text()').extract()
        #Sacar caracteres raros 
        contents = response.xpath('//*[@class="field-item even"]/div').extract()
        contenido = "" 
        for content in contents:
            description = re.sub('<.*?>', '', content)
            contenido = contenido + " " + description
        item = androidCentralItem()
        item["title"] = title[0]
        item["content"] = contenido
        yield item
