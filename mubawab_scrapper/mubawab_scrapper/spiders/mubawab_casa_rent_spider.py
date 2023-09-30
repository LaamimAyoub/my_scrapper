import scrapy


class MubawabCasaRentSpiderSpider(scrapy.Spider):
    name = "mubawab_casa_rent_spider"
    allowed_domains = ["www.mubawab.ma"]
    start_urls = ["https://www.mubawab.ma/fr/ct/casablanca/immobilier-a-louer"]

    def parse(self, response):
        pass
