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
            '//*[@id="grid_items"]/div[1]/div/h2/a/@href').extract()
        print("Links:", links)
        # We stored already crawled links in this list
        crawledLinks = []

        for link in links:
            # If it is a proper link and is not checked yet, yield it to the
            # Spider
            if link not in crawledLinks:
                #link = "http://www.androidcentral.com" + link
                crawledLinks.append(link)
                yield Request(link, self.parse)
        titles2 = response.xpath(
            '//*[@id="article-header"]/section/div/div/section/h1/text()').extract()
        titles = response.xpath(
            '//div[contains(@class, "teaser_main")]/h2/a/text()').extract()
        paginas = response.xpath(
            '//div[contains(@class, "teaser_main")]/h2/a/@href').extract()
        for pagina in paginas:
            print("página:", pagina)
        for title in titles:
            item = androidCentralItem()
            item["title"] = title
            yield item
