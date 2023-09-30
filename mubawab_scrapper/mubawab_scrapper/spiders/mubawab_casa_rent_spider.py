from os import link
import scrapy


class MubawabCasaRentSpiderSpider(scrapy.Spider):
    name = "mubawab_casa_rent_spider"
    allowed_domains = ["www.mubawab.ma"]
    start_urls = ["https://www.mubawab.ma/fr/ct/casablanca/immobilier-a-louer"]

    def parse(self, response):
        lii = response.css("li[class='listingBox w100']")
        for elt in lii:
            link_ref = elt.attrib.get('linkref')
            img_url = elt.css('div[class="photoBox col-5 floatR emptyCol"]')[0].attrib.get('data-url')
            title = elt.css('h2[class="listingTit"]')[0].css('a::text').extract_first()
            super_rooms = elt.css('h2[class="listingTit"]')[0].css('a::text').extract_first()
            location = elt.css('h3::text').extract_first()
            description =  elt.css('p[class="listingP descLi"]::text').extract_first()
            price = elt.css('span::text').extract_first()
            

            yield {
                "title": title,
                "superficie, chambres": super_rooms,
                "location": location,
                "description": description,
                "price": price,
                "link_ref": link_ref,
                "img_url": img_url
            }