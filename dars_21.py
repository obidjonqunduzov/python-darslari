# lambda dan foydalanamiz!

import math


kvadrat = lambda x,y : x ** y
print(kvadrat(3, 2))

def daraja(n):
	return lambda x: x ** n 

kvadrat2 = daraja(2)
print(kvadrat2(5))

# map ruyxat ichidagi elementlar bilan ishlaydi!

from math import sqrt

sonlar = list(range(11))
ildizlar = list(map(sqrt,sonlar)) # sonlar ichidagi har bir uzgaruvchini ildizini hisoblaydi
print(ildizlar)

def daraja_2(x):
	return x*x
print(list(map(daraja_2,sonlar)))

# yoki

kvadratlar = list(map(lambda x: x*x,sonlar))
print(kvadratlar) 

a = [4,5,6]
b = [7,8,9]
a_plus_b =list(map(lambda x,y: x+y, a,b))
print(a_plus_b)


import random as r #random sozini r deb qisqartirdim

raqamlar = r.sample(range(100),10) # 100ta raqam ichidan tasodifiy 10ta raqamni oladi!
print(raqamlar)


def juftmi(x):
	""" x juft bolsa True ,aks xolda x ni False qaytaradi"""
	return x%2 == 0
juft_raqamlar = list(filter(juftmi,raqamlar)) # filter royxat ichidagi elementlarni saralaydi
print(juft_raqamlar)

# yoki

juft_raqamlar = list(filter(lambda x: x%2==0, raqamlar ))
print(juft_raqamlar)