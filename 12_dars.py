# python lugati - davomi
# items() lugat ichidagi elementlar, agar biz lugat ichidagi elementlar qnchaligini bilmasak ushbu dasturdan foydalanamiz!

talaba = {
	'ism':'Obidjon',
	'familiya':'Qunduzov',
	'fakultet':'fiztex',
}

for kalit,qiymat in talaba.items():
	print(f"kalit soz: {kalit}")
	print(f'qiymat soz: {qiymat} \n')

telefonlar = {
	'ali':'iphone x',
	'vali':'galaxe s21 ultra',
	'olim':'redmi 10 pro',
	'obid':'honor'
}
for k,q in telefonlar.items():
	print(f"{k.title()} ning telefon modeli {q}")

mahsulotlar ={
	'olma': 10,
	'nok': 12,
	'anjir': 18,
	'uzum': 20
}

# keys() kalit degani

print("Dokonimizda bor mahsulotlar")
for mahsulot in mahsulotlar.keys():
	print(mahsulot.title())

# sorted() tartib bilan chiqarish

print("Dokonimizda bor mahsulotlar")
for mahsulot in sorted(mahsulotlar):
	print(mahsulot.title())

# values() faqat qiymatlarni chiqaradi

print('Foydalanuvchilar quyidagi telefonlarni ishlatishadi')
for tel in telefonlar.values():
	print(tel)

# set() bir necha takrorlanib kelgan bir xel malumotlarni bitta qilib chiqaradi

toys ={'car','ball','car','lamp'}
print(toys)

# Uyga vazifa

# 1

python_lugat = {
	'int':'son qiymati',
	'float':'onlik qiymat',
	'str':'matn',
	'Boolean':'mantiqiy qiymat',
	'if':'shartlarni tekshirish operatori'
}
for python,qiymat in sorted(python_lugat.items()):
	print(f"{python} - {qiymat}")

# 2

davlatlar = {
	'AQSH':'washington',
	'tajikistan':'dushanbe',
	'uzbekistan':'tashkent',
	'rossiya':'moskva',
	'Angliya':'london'
}
for davlat,poytaht in sorted(davlatlar.items()):
	print(f"{davlat.upper()}  {poytaht.title()}")

# 3

davlat_nomi = input("Istalgan davlatni kiriting: ")
davlatlar_poytahti = {

	'AQSH':'washington',
	'tajikistan':'dushanbe',
	'uzbekistan':'tashkent',
	'rossiya':'moskva',
	'Angliya':'london'
}

natija = davlatlar_poytahti.get(davlat_nomi, 'Bizda bunday davlat mavjud emas!')
print(natija)
	
# 4

restoran_menu = {
	'non': 5,
	'choy':3,
	'desert':15,
	'burger':25,
	'osh':20
}
savat = []
for n in range(3):
	savat.append(input(f'savatchaga {n+1} mahsulotlarni qoshing: '))

for buyurtma in savat:
	if buyurtma in restoran_menu:
		print(f"{buyurtma} ning narhi {restoran_menu[buyurtma]} somon")
	else:
		print(f"bizda bunday {buyurtma} yoq")