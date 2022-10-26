from scrapy import Spider, Request
from WebCrawler.items import AllocineItem
from WebCrawler.pipelines import AllocineScrapperPipeline

class AllocineSpider(Spider):
    name = 'allocine'
    allowed_domains = ['www.allocine.fr']
    #Liste des pages à collecter
    start_urls = [f'https://www.allocine.fr/film/meilleurs/?page={n}' for n in range(1,10)]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_allocine)
        
        
    def parse_allocine(self, response):
        # Instancie le pipeline
        pipeline = AllocineScrapperPipeline()
        base_name = 'allocine'
        table_name = 'film'
        base = pipeline.process_init_database(base_name)
        pipeline.process_create_table(base, table_name)
        liste_film = response.css('li.mdl') # liste l'ensemble des films
        
        # Boucle qui parcours l'ensemble des éléments de la liste des films
        for film in liste_film:
            item = AllocineItem()

            # Nom du film
            try:
                item['title'] = film.css('h2.meta-title a::text').get()
            except:
                item['title'] = 'None'
              
            # Lien de l'image du film
            try:
                item['img'] = film.css('img.thumbnail-img').attrib['src']
            except:
                item['img'] = 'None'


            # Auteur du film
            try:
                item['author'] = film.css('div.meta-body-direction a::text').get()
            except:
                item['author'] = 'None'
           
            # Durée du film
            try:
                item['time'] = film.css('div.meta-body-info::text')[0].get().strip()
            except:
                item['time'] = 'None'

            # Genre cinématographique
            try:
                item['genre'] = ' '.join([el.get() for el in response.css('div.meta-body-info')[0].css('span::text')[1:]])
            except:
                 item['genre'] = 'None'

            # Score du film
            try:
                item['score'] = film.css('div.rating-item span.stareval-note::text')[0].get()
            except:
                item['score'] = 'None'

            # Description du film
            try:
                item['desc'] = film.css('div.content-txt::text').get().strip()
            except:
                item['desc'] = 'None'

            # Date de reprise
            try:
                item['reprise'] = film.css('div.meta-body span.date::text').get()
            except:
                item['reprise'] = 'None'
            
            # Page
            try:
                item['page'] = response.url.split('page=')[-1]
            except:
                item['page'] = 1

            pipeline.process_add_row(base, table_name, item)
            
            yield item
