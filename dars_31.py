
# PIP VA TASHQI KUTUBXONALAR

from googletrans import Translator
tarjimon = Translator() # Translator bu maxsus klass (tarjimon esa obyekt)
matn_uz =input( ": ")
tarjima = tarjimon.translate(matn_uz)
print(tarjima.text)


import requests
from pprint import pprint

manzil= "https://kun.uz/news/main"
r = requests.get(manzil)
pprint(r.text)