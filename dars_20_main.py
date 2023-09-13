# Modulga qisqa nom berish 
# import dars_20_avto_info as dai(dars avto info) degan qisqartma
# from dars_20_avto_info import avto_info,avto_kirit,info_print shu yul orqali modul ichidagi funksiyalarni chaqirib olamiz!
# from dars_20_avto_info import *
# Diqqat! Bir necha sabablarga ko'ra bu usuldan foydalanish tavsiya qilinmaydi. 
#  Katta modullarda yuzlab funksiyalar bo'lishi mumkin, va funksiya nomi sizning dasturingizdagi boshqa funksiya yoki o'zgaruvchi bilan bir hil nomga ega bo'lsa, 
#   dastur xato ishlashiga olib keladi


from dars_20_avto_info import avto_info,avto_kirit,info_print

avto_1 = avto_info('Opel','qora','avtomat',2020,40000)
info_print(avto_1)

import math

x = 400
print(math.sqrt(x)) # qavus ichidagi sonni ildizini hisoblaydi!

print(math.pow(5,3)) # qavus ichidagi sonni , son darajasigacha kotaradi!

from math import pi

print(pi)

print(math.log2(8))
print(math.log10(100))

# random Moduli

import random as ran # random sozini qisqartirib ran deb oldek

son = ran.randint(0,100)
print(son)


# choice(x)
# x ning ichidan tasodifiy qiymatni qaytaruvchi funksiya.
# Bunda x bir necha elementdan iborat o'zgaruvchi (matn, ro'yxat) bo'lishi kerak.

ismlar = ['olim','obid','hasan','husan']
ism = ran.choice(ismlar) # ismlardan tasodifiy ism tanlaymiz
print(ism)
print(ran.choice(ism)) # ism ichidan tasodifiy harf tanlaymiz! 

x = list(range(1,5,54))
print(x)
print(ran.choice(x))


x = list(range(11,10))
print(x)
ran.shuffle(x)
print(x)