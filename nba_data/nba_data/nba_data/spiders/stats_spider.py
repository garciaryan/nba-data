import scrapy


class StatsSpider(scrapy.Spider):
    name = "stats"

    def start_requests(self):
        urls = [
            'https://stats.nba.com/players'
        ]