# Python standart kutubxonasi bilan ishlash

import datetime as dt

hozir = dt.datetime.now()
print(hozir) # HOZIRGI VAQTNI KO'RSATADI

# SANANI AJRATIB OLISH UCHUN
print(f"Hozirgi real kun: {hozir.date()}")

# SOATNI AJRATIB OLISH UCHUN
print(f"Hozirgi real vaqt: {hozir.time()}")

# KELAJAKDAGI VAQTNI ISHLATISH UCHUN

bugun = dt.datetime.today()
ramazan = dt.datetime(2024, 3, 11)
farq = ramazan - bugun
print(f"Ramazon oyiga {farq.days} kun va qoldi InshaAlloh!")


import math 


PI = math.pi
print(f"pi ning qiymati: {PI}")

E = math.e
print(f"E ning qiymati:  {E}")

Log = math.log10(100)
print(Log)


# Sonlarni yaxlitlash

x = 4.6

print(math.ceil(x)) # Sonni bitta ko'paytirib yaxlitlaydi
print(math.floor(x)) # Sonni bitta kamaytirib yaxlitlaydi


# Ildiz va Darajaga ko'tarish

x = 25
print(math.sqrt(x)) # x ning ildiz sonini ko'rsatadi

# yoki darajaga ko'taradi

print(math.pow(x,2)) # x ning kvadratiga ko'taradi


# Chiroyli print qilib chiqaish uchun

from pprint import pprint
import json

filename = "C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\json_fayl\\bemor.json"
with open(filename) as f:
	bemor = json.load(f)

print(f"{bemor} \n") # bu oddiy print

pprint(bemor) # bu chiroyli print


# RegEx andoza yordamida matn izlash

import re

word1 = 'темир'
word2 = 'томир'
word3 = 'тулпор'

andoza ='^т...р$'

print(re.match(andoza,word1))
print(re.match(andoza,word2))
print(re.match(andoza,word3))

from uzwords import words

andoza ='^б....а$'
matches = []

for word in words:
	if re.match(andoza,word):
		matches.append(word)
print(matches)


matn = """Вы всегда можете задать нам любой вопрос в разделе Обращения 
в Личном кабинете или воспользоваться одним из мессенджеров
Чтобы рассылка не попадала в спам, добавьте info@wildberries.ru в адресную книгу"""

andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\\.[^@ \t\r\n]+'

email = re.findall(andoza,matn)
print(email)


# Kuchli parolni tekshirish
# Quyidagi andoza ham ihateregex.io sahifasidan olindi
andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = "Yangi parol kiriting"
msg += '(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, '
msg += '1 ta son va 1 ta maxsus belgi boʻlishi kerak): '

while True:
    password = input(msg)
    if re.match(andoza,password):
        print("Maxfiy so'z qabul qilindi")
        break
    else:
        print("Maxfiy so'z talabga javob bermadi")