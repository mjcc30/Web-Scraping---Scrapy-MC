# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class AllocineItem(Item):
     # Nom du film
    title   = Field()
    # Lien de l'image du film
    img     = Field()
    # Auteur du film
    author  = Field()
    # Durée du film
    time    = Field()
    # Genre cinématographique
    genre   = Field()
    # Score du film
    score   = Field()
    # Description du film
    desc    = Field()
    # Date de reprise
    reprise = Field()
    # Numéro de page
    page    = Field()

class BoursoramaItem(Item):
    # indice boursier
    indice = Field()
    # indice cours de l'action
    cours  = Field()
    # Variation de l'action
    var    = Field()
    # Valeur la plus haute
    hight  = Field()
    # Valeur la plus basse
    low    = Field()
    # Valeur d'ouverture
    open   = Field()
    # Date de la collecte
    time   = Field()

class MyAnimeListItem(Item):
    # nom des animés
    title = Field()
    # image des animés
    img   = Field()
    # description des animés
    desc  = Field()