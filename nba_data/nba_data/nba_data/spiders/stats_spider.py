import scrapy
from selenium import webdriver
from nba_data.nba_data.items import PlayerStats


class StatsSpider(scrapy.Spider):
    name = "stats"
    allowed_domains = ["stats.nba.com"]
    start_urls = ('https://stats.nba.com/leaders',)

    def __init__(self):
        self.driver = webdriver.Chrome()

    def parse(self, response):
        self.log('Scraping...')
        self.driver.implicitly_wait(7)
        self.driver.get(response.url)

        while True:
            item = PlayerStats()
            next = self.driver.find_element_by_tag_name('tr')

            try:
                for row in response.xpath('//tr/td'):
                    yield {
                        'player': row.css('td.player a::text').extract_first(),
                        'points': row.css('td::text')[4].extract_first(),
                        'assists': row.css('td::text')[18].extract_first(),
                        'rebounds': row.css('td::text')[16].extract_first(),
                        'steals': row.css('td::text')[19].extract_first(),
                        'blocks': row.css('td::text')[20].extract_first(),
                        'turnovers': row.css('td::text')[21].extract_first(),
                        'fgm': row.css('td::text')[5].extract_first(),
                        'fga': row.css('td::text')[6].extract_first(),
                        '3pm': row.css('td::text')[8].extract_first(),
                        '3pa': row.css('td::text')[9].extract_first(),
                        'minutes': row.css('td::text')[3].extract_first()
                    }
                next.click()
                print(response.body)
                self.log('Scraped.')
                exit(200)
            except:
                break
