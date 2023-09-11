# Funksiyalar bilan ishlash va funksiyaga ruyxat uzatish

def bahola(ismlar):
	baholar = {}
	while ismlar:
		ism = ismlar.pop()
		baho = input(f"Talaba {ism.title()} ning bahosini kiriting: ")
		baholar[ism] = int(baho)
	return baholar
talabalar = ['ali','vali','hasan','husan']
baholar = bahola(talabalar[:]) # nusxa olish [:]
print(baholar)
print(talabalar) # funksiyada ruyxatlar bilan ishlashda ixtiyot bulish kerak, chunki hozir (baholar) va (talabalar) bitta ruyxatga ikkita uzgaruvchini boglab quydek!

# Uyga vazifa 

# 1

def katta_harf(matnlar):
	matnlar = matnlar[:]
	for i in range(len(matnlar)):
		matnlar[i] = matnlar[i].title()
	return matnlar

ismlar = ['ali','vali','obid','olim']
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)

# 2

def bahola(ismlar):
	baholar = {}
	
	for ism in ismlar:
		baho = input(f"Talabalarni baxolash {ism.title()} ning bahosi : ")
		baholar[ism]=baho
	return baholar

baholar = bahola(talabalar)
print(baholar)
print(talabalar)