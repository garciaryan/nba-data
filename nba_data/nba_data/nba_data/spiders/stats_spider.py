import scrapy
import time
from selenium import webdriver


class StatsSpider(scrapy.Spider):
    name = "stats"
    allowed_domains = ["stats.nba.com"]
    start_urls = ('https://stats.nba.com/leaders',)

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(7)

    def parse(self, response):
        self.driver.get(response.url)

        while True:
            next = self.driver.find_element_by_tag_name('tr')

            try:
                page = response.url.split("/")[-2]
                filename = 'stats-%s.html' % page
                with open(filename, 'wb') as f:
                    f.write(response.body)
                time.sleep(7)
                next.click()
            except:
                break

    #def parse_stats(self, response):




