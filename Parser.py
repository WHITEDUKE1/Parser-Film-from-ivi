"""by WHITE DUKE"""
import requests
from bs4 import BeautifulSoup as BS
from time import sleep
from random import randint,shuffle


class Film:

    def __init__(self):
        def random_num():
            random_num = []
            for i in range(150):
                random_num.append(randint(1, 1000) + 481870)
            shuffle(random_num)
            return random_num

        self.random_num = random_num()

        self.rating_and_film = []

        self.amount_film = 30

        self.i = 0

    def parse_film(self):
        while True:

            try:

                if len(self.rating_and_film) >= self.amount_film:
                    break

                r = requests.get(f"https://www.ivi.ru/watch/{self.random_num[self.i]}")

                html = BS(r.content, 'html.parser')

                name_film = str(html.select("#root > section > div > div > div > div > div.contentCard__info > div.watchTitle.contentCard__watchTitle > h1")).split('>')[1].split('<')[0].split('-')[0]

                rating_film = str(html.select("#root > section > div > div > div > div > div.contentCard__info > div.ratingMobile.contentCard__ratingMobile > div > div.ratingMobile__nbl-ratingPlate.nbl-ratingPlate.nbl-ratingPlate_style_xadus.nbl-ratingPlate_size_wyrms > div")).split('>')[1].split('<')[0].replace(',', '.')

                self.rating_and_film.append(f'{name_film} ===> {rating_film}⭐\n')

                self.i += 1

                sleep(0.001)

            except:
                self.i += 1

        for i in range(len(self.rating_and_film)-1):
            for j in range(len(self.rating_and_film)-i-1):
                if float(self.rating_and_film[j].split('===> ')[1].split('⭐')[0]) > float(self.rating_and_film[j+1].split('===> ')[1].split('⭐')[0]):
                    self.rating_and_film[j], self.rating_and_film[j+1] = self.rating_and_film[j+1], self.rating_and_film[j]

        self.rating_and_film.reverse()





