# 30 dars uyga vazifa

# 1
# Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring

import datetime as dt
import math

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