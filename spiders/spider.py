import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from prueba0.items import Prueba0Item
from scrapy.exceptions import CloseSpider

class prueba0Spider(CrawlSpider):
    name = 'prueba0' # Nombre a utilizar cuando vayamos a utilizar el script
    item_count = 0
    allowed_domain = ['www.amazon.com.mx'] #Que no salga de este dominio
    start_urls = ['https://www.amazon.com.mx/s?k=celulares&__mk_es_MX=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=TUJ2ZAGZDXLL&sprefix=celulares%2Caps%2C882&ref=nb_sb_noss'] #Dominio donde iniciará el web scraping

    rules = {
        Rule(LinkExtractor(allow=(), restrict_xpaths= ('//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]') )),
        Rule(LinkExtractor(allow=(), restrict_xpaths= ('//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-4"]') ),
                            callback='parse_item', follow = False)        
    }

    def parse_item(self, response):
        prueba0_item = Prueba0Item()
        #info del producto
        prueba0_item['nombre'] = response.xpath('normalize-space(//*[@id="productTitle"]/text())').extract()
        prueba0_item['precio'] = response.xpath('normalize-space(//*[@id="corePrice_feature_div"]/div/span/span[1]/text())').extract()
        prueba0_item['envio'] = response.xpath('normalize-space(//*[@id="mir-layout-DELIVERY_BLOCK-slot-PRIMARY_DELIVERY_MESSAGE_LARGE"]/span/a/text())').extract()
        prueba0_item['estrellas'] = response.xpath('normalize-space(//*[@id="reviewsMedley"]/div/div[1]/div[2]/div[1]/div/div[2]/div/span/span/text())').extract()

        #Info de la tienda
        prueba0_item['nom_tienda'] = response.xpath('normalize-space(//*[@id="bylineInfo"]/text())').extract()
        prueba0_item['url_tienda'] = response.xpath('normalize-space(//*[@id="bylineInfo"]/@href/text())').extract()

        self.item_count +=1

        if self.item_count > 20:
            raise CloseSpider('item_exceeded')
        yield prueba0_item
      


