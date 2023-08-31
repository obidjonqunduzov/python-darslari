# lugatlar bilan ishlash!
# {} kalit soz 
cars = {'model':'Rangr Rover', 'rang':'black'}
print(cars['model'])
print(cars['rang'])

en_uz = {'apple':'olma', 'banana':'banan','apricot':'orik'}
print(en_uz['apricot'])

mevalar = {'olma':10, 'qovun':15, 'uzum':8}
print(f"Olma narhi {mevalar['olma']} somon")

talaba = {'ism':'obidjon qunduzov','yoshi':25,'t_yili':1998}
print(f"{talaba['ism'].title()},\
	  {talaba['t_yili']} tugilgan,\
	  {talaba['yoshi']} yoshda")
# yangi kalit soz!
talaba['kurs'] = 4
talaba['fakultet'] = 'fiztex'
print(talaba)

talaba_1 = {}
talaba_1['yosh'] = 20
talaba_1['t_yili'] = 1998
talaba_1['ismi'] = 'Obidjon'
print(talaba_1)

# biror aperatorni uchirish uchun del dan foydalanamiz!

del talaba_1['yosh']
print(talaba_1)

avtomobillar ={
	'ali':'mers',
	'vali':'opel',
	'olim':'bmw',
	'obid':'ferrari'
}
print(f"{avtomobillar['obid']}")

# lugatimizda biz kiritgan klyuch sozi bolmasa unda get() dan foydalanamiz!

avtomobil = avtomobillar.get('Hasan', 'Bunday ism mavjud emas')
print(avtomobil)

# Uyga vazifa

# 1

otam = {
	'yoshlari': 47,
	'kasblari': 'oqituvchi',
	'ismlari': 'komiljon'
}

onam = {
	'yoshlari': 47,
	'kasblari': 'uy bekasi',
	'ismlari': 'Hikoyat'
}
print(f"Otamnning ismlari {otam['ismlari'].title()}, {otam['yoshlari']} yoshdalar, kasblari {otam['kasblari']}")
print(f"Onamning ismlari  {onam['ismlari'].title()}, {onam['yoshlari']} yoshdalar, kasblari {onam['kasblari']}")

# 2

taomlar ={
	'akam':'osh',
	'otam':'norin',
	'onam':'shirgurunch',
	'ayolim':'sambusa'
}
print(f"Mening oila azolarim quyidagi taomlarni sevib estemol qilishadi:{taomlar['akam']},{taomlar['otam']},{taomlar['onam']}")

# 3

python_lugat ={
	'str':'matn',
	'int':'son',
	'float':'onlik son',
	'list':'list',
	'for':'uchun',
	'if':'agar'
}
print(f" {python_lugat['str']} \n {python_lugat['for']} \n {python_lugat['if']}")

# 4

python =input("Biror soz kiriting: ")
python_1 = python_lugat.get(python, 'Bunday soz mavjud emas')
print(python_1)

# 5

en_uz_tarjima ={
	'book':'kitob',
	'room':'xona',
	'father':'ota',
	'beach':'sohil',
	'peach':'shaftoli'
}

soz_kiriting = input("kalit sozini kiriting: ")
tarjima = en_uz_tarjima.get(soz_kiriting)
if tarjima == None:
	print('Bunday soz lugatimizdan topilmadi!')
else:
 	print(f"{soz_kiriting.title()} sozi  {tarjima.title()} deb tarjima qilinadi")