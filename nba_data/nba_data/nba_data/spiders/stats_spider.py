import scrapy


class StatsSpider(scrapy.Spider):
    name = "stats"

    def start_requests(self):
        urls = [
            'https://stats.nba.com/leaders'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'stats-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
