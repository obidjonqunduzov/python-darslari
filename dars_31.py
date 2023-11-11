# python kutubxonasi bilan ishlash

from googletrans import Translator
tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)
matn_uz = "Python - dunyodagi eng mashxur dasturlash tili"
tarjima = tarjimon.translate(matn_uz)
print(tarjima.text)

tarjima_ru = tarjimon.translate(matn_uz, dest='ru')
print(tarjima_ru.text)

matn_en = "Tashkent is the capital of Uzbekistan"
tarjima_uz = tarjimon.translate(matn_en, dest='uz')
print(tarjima_uz.text)

import requests
from pprint import pprint

manzil= "https://kun.uz/news/main"
r = requests.get(manzil)
pprint(r.text)

country = "Uzbekistan"
url = f"https://restcountries.eu/rest/v2/name/{country}"
r = requests.get(url)
r_json = r.json()[0]
print(r_json['capital'])

import requests
from bs4 import BeautifulSoup

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)


soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_="news-title") # yangiliklarning mavzusini ajratib olamiz
print(news[0].text) # eng birinchi yangilikni konsolga chiqaramiz