# Funksiyalar  bilan ishlash!

def salom_ber(ism):
	"""Salom beruvchi funksiya"""
	print(f"Assalomu alaykum! hurmatli {ism.title()}")
salom_ber('Hasam')
salom_ber("Olim")

def toliq_ism(ism,familiya):
	"""Foydalanuvchi ism va familiasini jamlab chiqaruvchi dastur"""
	print(f"Foydalanuvchi ismi: {ism.title()}\n")
	print(f"Foydalanuvchi familiyasi: {familiya.title()}")

toliq_ism('olim', 'hakimov')

def yosh_hisobla(ism,tugilgan_yil): # bu parametr qanday ketma-ketligda yozilsa konsolga ham shunday chiqadi!
	"""Foydalanuvchi yoshini hisoblovchi dastur"""
	print(f"{ism.title()} {2023 - tugilgan_yil} yoshda")

yosh_hisobla('Obidjon',1998) # ketma ketligini togri kiritish kerak
# yosh_hisobla(1998, 'Obidjon') # bu xato!
# yoki
yosh_hisobla(tugilgan_yil=1998,ism='Obidjon')

def t_yilini_hisobla(ism,familiya,joriy_yil=2023,):
	"""Foydalanuvchining tugilgan yilini hisoblaydi"""
	print(f"Foydalanuvchi: {ism.title()} {familiya.title()} {joriy_yil -25 } tugilgan")
t_yilini_hisobla('Obidjon','Qunduzov', )