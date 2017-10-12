import scrapy
from selenium import webdriver
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
from nba_data.items import PlayerStats


class StatsSpider(scrapy.Spider):
    name = "stats"
    allowed_domains = ["stats.nba.com"]
    start_urls = ('https://stats.nba.com/leaders',)

    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.log('Scraping...')
        self.driver.get(response.url)
        items = []

        while True:

            for row in response.xpath('//tr//td'):
                item = PlayerStats()
                item['player'] = row.css('td.player a::text').extract()
                item['points'] = row.css('td::text')[4].extract()
                item['assists'] = row.css('td::text')[18].extract()
                item['rebounds'] = row.css('td::text')[16].extract()
                item['steals'] = row.css('td::text')[19].extract()
                item['blocks'] = row.css('td::text')[20].extract()
                item['turnovers'] = row.css('td::text')[21].extract()
                item['fgm'] = row.css('td::text')[5].extract()
                item['fga'] = row.css('td::text')[6].extract()
                item['3pm'] = row.css('td::text')[8].extract()
                item['3pa'] = row.css('td::text')[9].extract()
                item['minutes'] = row.css('td::text')[3].extract()
                items.append(item)
                yield items

            next = self.driver.find_element_by_tag_name('tr')

            try:
                next.click()
                self.log('Scraped.')
                exit(200)
            except:
                break
