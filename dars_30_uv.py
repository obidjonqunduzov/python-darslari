# 30 dars uyga vazifa

# 1
# Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring

import datetime as dt
from pprint import pprint
import json
import math
import re

bugun = dt.datetime.now() 


ertaga = dt.datetime(2024,11,6)
farq = ertaga - bugun

print(farq)

# 2
# Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring

qurbon = dt.datetime(2024,6,16)
ramazan = dt.datetime(2024, 3, 11)

farq_ramazon = ramazan - bugun
farq_qurbon = qurbon - bugun

print(f"Ramazon oyigacha {farq_ramazon.days} kun  qoldi InshaAlloh!")
print(f"Qurbon hayitigacha  {farq_qurbon.days} kun  qoldi InshaAlloh!")


# 3 
# Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi funksiya yozing

tugulgan_kun = dt.datetime(1998,10,10)

farq_tugulgan_kun = bugun - tugulgan_kun

print(f"Meni dunyoga kelganimga {math.floor(farq_tugulgan_kun.days/365)} yil bo'ldi")
print(f"Meni dunyoga kelganimga {math.floor(farq_tugulgan_kun.days/12)} oy bo'ldi")
print(f"Meni dunyoga kelganimga {math.floor(farq_tugulgan_kun.days/1)} kun bo'ldi")

# 4
# Foydalanuvchidan telefon raqamini kiritishni so'rang. Kiritlgan qiymatni andoza yordamida tekshiring

nomer = "Telefon raqamingizni kiriting: "
andoza_tel = '^\\+[1-9]\\d{1,14}$'

while True:
	telefon = input(nomer)
	if re.match(andoza_tel,telefon):
		print(f"Sizning {telefon} nomeringiz qabul qilindi")
		break
	else:
		print(f"Xato {andoza_tel}, telefon raqamingizni kiriting!")

# 5
# Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya yozing. Quyidagi matndan namuna sifatida foydalanishingiz mumkin:

matn = """
Carrier	SMS Gateway Domain	MMS Gateway Domain
AT&T	number@txt.att.net	number@mms.att.net
Boost Mobile	number@sms.myboostmobile.com	number@myboostmobile.com
Cricket Wireless	number@mms.cricketwireless.net	number@mms.cricketwireless.net
Google Project Fi	number@msg.fi.google.com	number@msg.fi.google.com
Republic Wireless	number@text.republicwireless.com	None
Sprint	number@messaging.sprintpcs.com	number@pm.sprint.com """

andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\\.[^@ \t\r\n]+'

ip_adress = re.findall(andoza,matn)
pprint(ip_adress)

