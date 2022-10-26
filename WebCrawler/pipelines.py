# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# Import de la class DataBase permettant de créer des bases de données
from WebCrawler.utils.database import DataBase
# Import du package sqlalchemy permetant de gérer les bases de données
import sqlalchemy as db

class AllocineScrapperPipeline:
    # Instaciation de la base de données
    def process_init_database(self, base_name):
        return DataBase(base_name)

    # Création de la table
    def process_create_table(self, base, table_name):
        base.create_table(table_name, 
                 title=db.String,
                 img=db.String,
                 author=db.String,
                 time=db.String,
                 genre=db.String,
                 score=db.String,
                 desc=db.String,
                 reprise=db.String,
                 page=db.String
                 )

    # Ajout d'une ligne dans la base de données
    def process_add_row(self, base,table_name, item):
        base.add_row(table_name,
            title=item['title'],
            img=item['img'],
            author=item['author'],
            time=item['time'],
            genre=item['genre'],
            score=item['score'],
            desc=item['desc'],
            reprise=item['reprise'],
            page=item['page'],
            )

class BoursoramaScrapperPipeline:
    # Instaciation de la base de données
    def process_init_database(self, base_name):
        return DataBase(base_name)

    # Création de la table
    def process_create_table(self, base, table_name):
        base.create_table(table_name,
                 indice=db.String,
                 cours=db.String,
                 var=db.String,
                 hight=db.String,
                 low=db.String,
                 open=db.String,
                 time=db.String
                 )

    # Ajout d'une ligne dans la base de données
    def process_add_row(self, base,table_name, item):
        base.add_row(table_name,
            indice=item['indice'],
            cours=item['cours'],
            var=item['var'],
            hight=item['hight'],
            low=item['low'],
            open=item['open'],
            time=item['time']
            )

class MyAnimeListScrapperPipeline:
    # Instaciation de la base de données
    def process_init_database(self, base_name):
        return DataBase(base_name)

    # Création de la table
    def process_create_table(self, base, table_name):
        base.create_table(table_name, 
                 title=db.String,
                 img=db.String,
                 desc=db.String
                 )

    # Ajout d'une ligne dans la base de données
    def process_add_row(self, base,table_name, item):
        base.add_row(table_name,
            title=item['title'],
            img=item['img'],
            desc=item['desc'],  
            )