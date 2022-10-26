from cmath import pi
from scrapy import Spider, Request
from WebCrawler.items import MyAnimeListItem
from WebCrawler.pipelines import MyAnimeListScrapperPipeline

class MyanimelistSpider(Spider):
    name = 'myanimelist'
    allowed_domains = ['myanimelist.net']
    alpha_list = ['.','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    #Liste des pages à collecter
    start_urls = [f'https://myanimelist.net/manga.php?letter={n}' for n in alpha_list]
    # start_urls = [f'https://myanimelist.net/manga.php?letter=a']


    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse_allocine)
        
        
    def parse_allocine(self, response):
        # Instancie le pipeline
        pipeline = MyAnimeListScrapperPipeline()
        base_name = 'myanimelist'
        table_name = 'manga'
        base = pipeline.process_init_database(base_name)
        pipeline.process_create_table(base, table_name)

        # liste l'ensemble des animés
        list_anime = response.css('div.js-categories-seasonal tr')[1:]
        
        # Boucle qui parcours l'ensemble des éléments de la liste des films
        for anime in list_anime:
            item = MyAnimeListItem()

            # Nom de l'animé
            try:
                item['title'] = anime.css('td a strong::text').get()
            except:
                item['title'] = 'None'
              
            # Lien de l'image de l'animé
            try:
                item['img'] = anime.css('div.picSurround img').attrib['data-src']
            except:
                item['img'] = 'None'


            # Description de l'animé
            try:
                item['desc'] = anime.css('div.pt4::text').get()
            except:
                item['desc'] = 'None'
            
            # Letter
            # try:
            #     item['page'] = response.url.split('letter=')[-1]
            # except:
            #     item['page'] = 1

            # Page

            pipeline.process_add_row(base, table_name, item)

            yield item