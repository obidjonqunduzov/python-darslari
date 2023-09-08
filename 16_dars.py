# Funksiyalar  bilan ishlash!

def salom_ber(ism):
	"""Salom beruvchi funksiya"""
	print(f"Assalomu alaykum! hurmatli {ism.title()}")
salom_ber('Hasan')
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

# Uyga vazifa

# 1

def yoshini_hisoblash(ism,familiya,foy_yoshi):
	""" Foydalanuvchini ism,familiyasi va yoshini surab unning tugilgan yilini topish"""
	print(f"{ism.title()} {familiya.title()} , {2023 - foy_yoshi }")

yoshini_hisoblash('Obidjon','Qunduzov',25)

# 2

def foy_son(son):
	"""Foydalanuvchi kiritgan sonni kvadrati va kubini hisoblash """
	print(f"kvadrati = {son**2} ")
	print(f"kubi = {son**3}")
foy_son(5)

# 3

def juft_toq(sonlar):
	"""sonlarni juft yoki toq ekanligini hisoblaydi """
	if sonlar % 2 == 0:
		print(f"{sonlar}- juft son")
	else:
		print(f"{sonlar} toq son")
juft_toq(18)

# 4

def katta_kichik(katta_sonlar,kichik_sonlar):
	"""sonlarni bir-biridan katta yoki kichigligini hisoblaydi"""
	if katta_sonlar > kichik_sonlar:
		print(f"kichik {kichik_sonlar} dan {katta_sonlar}")
	elif katta_sonlar == kichik_sonlar:
		print(f"teng  {katta_sonlar} ga {kichik_sonlar}")
	else:
		print(f"katta {katta_sonlar} dan {kichik_sonlar}")

katta_kichik(30,30)

# 5,6

def x_y(x,y=2):
	print(f"{x} ning {y} darajasi = {x**y}")
x_y(10,2)
x_y(4,2)
x_y(2,3)
x_y(5,3)

# 7

def qoldiqsiz_son(sonlar):
	"""Foydalanuvchi kiritgan son 1-10 gacha qaysi sonlarga qoldiqsiz bolinadi"""
	for son in range(1,11):
		if not  sonlar%son:
			print(f"{sonlar} - {son} ga qoldiqsiz bolinadi")
qoldiqsiz_son(135)
	

