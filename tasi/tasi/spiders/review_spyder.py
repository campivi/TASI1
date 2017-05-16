from scrapy.spiders import Spider
from scrapy.http import Request
from tasi.items import androidCentralItem
import re


class review_spyder(Spider):
    name = "androidcentral"
    allowed_domains = ["androidcentral.com"]
    start_urls = ["http://www.androidcentral.com/search/xperia%20xz?query=xperia%20xz"]

    def parse(self, response):
        links = response.xpath('//*[@id="grid_items"]/div[1]/div/h2/a').extract()
        print(links)
        # We stored already crawled links in this list
        crawledLinks = []

        # Pattern to check proper link
        # I only want to get the tutorial posts
        #linkPattern = re.compile("^\/tutorials\?page=\d+")

        for link in links:
            # If it is a proper link and is not checked yet, yield it to the
            # Spider
            if link not in crawledLinks:
                #link = "http://www.androidcentral.com" + link
                crawledLinks.append(link)
                yield Request(link, self.parse)

        titles = response.xpath(
            '//div[contains(@class, "teaser_main")]/h2/a/text()').extract()
        for title in titles:
            item = androidCentralItem()
            item["title"] = title
            yield item
