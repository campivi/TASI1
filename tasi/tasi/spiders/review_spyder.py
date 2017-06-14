from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from tasi.items import androidCentralItem
import re


class review_spyder(Spider):
    name = "libre"
    allowed_domains = ["elandroidelibre.elespanol.com"]
    start_urls = [
        "https://elandroidelibre.elespanol.com/?s=xperia+xz"]

    def parse(self, response):
        links = response.xpath(
            '/html/body/div[4]/section/article/a/@href').extract()
        print("Links:", links)
        # We stored already crawled links in this list
        crawledLinks = []
        linkPattern = re.compile("^https://elandroidelibre.elespanol.com/+")
        for link in links:
            # If it is a proper link and is not checked yet, yield it to the
            # Spider
            if (linkPattern.match(link)) and (link not in crawledLinks):
                #link = "https://elandroidelibre.elespanol.com" + link
                crawledLinks.append(link)
                yield Request(link, self.parse_page)

    def parse_page(self, response):
        title = response.xpath(
            '//*[@id="singlePostTitle"]/a').extract()
        #Sacar caracteres raros 
        contents = response.xpath('//p').extract()
        contenido = ""  
        for content in contents:
            description = re.sub('<.*?>', '', content)
            contenido = contenido + " " + description
        item = androidCentralItem()
        item["title"] = title[0]
        item["content"] = contenido
        yield item
