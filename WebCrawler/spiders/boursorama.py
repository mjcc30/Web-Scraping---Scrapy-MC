from scrapy import Spider, Request
from WebCrawler.items import BoursoramaItem
from datetime import datetime
from WebCrawler.pipelines import BoursoramaScrapperPipeline

class BoursoramaSpider(Spider):
    name = 'boursorama'
    allowed_domains = ['www.boursorama.com']
    #Liste des pages à collecter
    start_urls = [f'https://www.boursorama.com/bourse/actions/palmares/france/page-{n}?france_filter%5Bmarket%5D=1rPCAC' for n in range(1,4)]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_boursorama)
            
    def parse_boursorama(self, response):
        # Instancie le pipeline
        pipeline = BoursoramaScrapperPipeline()
        base_name = 'boursorama'
        table_name = 'action'
        base = pipeline.process_init_database(base_name)
        pipeline.process_create_table(base, table_name)

        # liste l'ensemble des actions
        liste_indices = response.css('tr.c-table__row')[1:]
        
        for indice in liste_indices:
            item = BoursoramaItem()
            
            # Indice boursier
            try: 
              item['indice'] = indice.css('a::text').get()
            except:
              item['indice'] = 'None'
            
            # Indice cours de l'action
            try: 
              item['cours'] = indice.css('span.c-instrument--last::text').get().strip()
            except:item['cours'] = 'None'
            
            # Variation de l'action
            try: 
              item['var'] = indice.css('span.c-instrument--instant-variation::text').get().strip()
            except:
              item['var'] = 'None'
            
            # Valeur la plus haute
            try: 
              item['hight'] = indice.css('span.c-instrument--high::text').get().strip()
            except:
              item['hight'] = 'None'
            
            # Valeur la plus basse
            try: 
              item['low'] = indice.css('span.c-instrument--low::text').get().strip()
            except:
              item['low'] = 'None'

            # Valeur d'ouverture
            try: 
              item['open'] = indice.css('span.c-instrument--open::text').get().strip()
            except:
              item['open'] = 'None'

            # Date de la collecte
            try: 
              item['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            except:
              item['time'] = 'None'

            pipeline.process_add_row(base, table_name, item)
            yield item
