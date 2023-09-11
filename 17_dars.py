
# Funksiya qiymati bilam ishlash

def toliq_ism_yasa(ism,familiya):
	# toliq ism qaytaruvchi funksiya
	toliq_ism = f"{ism} {familiya}"
	return(toliq_ism) # return(qaytarish) degani

toliq_ism_yasa("Obid",'Qunduzov')
talaba = toliq_ism_yasa("Obid","Qunduzov")
print(talaba)

def toliq_ism_yasa(ism,familiya,otasini_ismi=''):

	if otasini_ismi:
		toliq_ism = f'{ism} {familiya} {otasini_ismi}'
	else:
		toliq_ism =f'{ism} {familiya}'
	return toliq_ism.title()	

talaba1 = toliq_ism_yasa("olim","hakimov")
talaba2 = toliq_ism_yasa('obid','Qunduzov','komiljonovich')
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

def avto_info(kompaniya, model, rangi, karobka, yili, narhi = None):
	avto ={
	'kompaniya':kompaniya,
	'model':model,
	'rangi':rangi,
	'karobka':karobka,
	'yili':yili,
	'narh':narhi
	}
	return avto

avto_1 = avto_info('opel','infinity','qora','avtomat',2020)
avto_2 = avto_info('opel','astra','oq','mexanik',2018,12000)
avtolar = [avto_1, avto_2]
print("Onlayn bozordagi mavjud avtomashinalar: ")

for avto in avtolar:
	if avto['narh']:
		narh = avto['narh']
	else:
		narh = 'Nomalum'
	print(f"{avto['rangi']} {avto['model']}. Narhi: {narh}")

def oraliq(min,max,qadam):
	sonlar = []
	while min<max:
		sonlar.append(min)
		min += 1
	return sonlar
print(oraliq(0,11,2))
print(oraliq(11,21,2))

print("Saytimizda avtomobillar ruyxatini shakllantiramiz!")

avtolar = []
while True:
	print("\n Quyidagi malumotlarni kiriting", end = '')
	kompaniya = input("\n Ishlab chiqaruvchi: ")
	model = input("Modeli: ")
	rangi = input("Rangi: ")
	karobka = input("Karobka: ")
	yili = input("Yili: ")
	narhi = input("Narhi: ")
	avtolar.append(avto_info(kompaniya,model,rangi,karobka,yili,narhi))

	javob = input("Yana avto qoshasizmi? (ha/yoq): ")
	if javob == 'yoq':
		break
print("Salondagi avtomoshinalar: ")

for avto in avtolar:
	if avto['narh']:
		 narh = avto['narh']
	else:
		 narh = 'Nomalum'
	print(f"{avto['rangi'].title()} {avto['model'].title()} {avto['karobka']} karobka, Narh: {narh}")


# Uyga vazifa

# 1

def foydalanuvchi_info(ism,familiya,t_yili,t_joyi,email='',telefon=None,):

 	foydalanuvchi={
 	'ism':ism,
 	'familiya':familiya,
 	't_yili':t_yili,
 	't_joyi':t_joyi,
 	'emaoil':email,
 	'telefon':telefon,
 	}
 	return foydalanuvchi


print("Uz malumotlaringizni kiriting")

foydalanuvchilar = []

while True:
	
	ism = input("Ismingiz: ")
	familiya = input("Familiyangiz:")
	t_yili = input("Tugilgan yilingiz: ")
	t_joyi = input("Tugilgan joyingiz: ")
	email =input("email pochtangiz: ")
	telefon = input("Telefon raqamingiz: ")
	foydalanuvchilar.append(foydalanuvchi_info(ism,familiya,t_yili,t_joyi,email,telefon))
	javob = input("Yana malumot qoshasizmi? (ha/yoq): ")
	if javob == 'yoq':
		break
		
	print("foydalanuvchilar: ")

for foydalanuvchi in foydalanuvchilar:
	print(
		f"{foydalanuvchi['ism'].title()} {foydalanuvchi['familiya'].title()}",
		f" {foydalanuvchi['t_yili']} tugilgan, telefoni : {foydalanuvchi['telefon']}"
		)

# 2

def son(x,y,z):
	print(f"Eng katta qiymat {x}{y}{z}")
	max = x
	if y>max:
		max =y
	if z>max:
		max=z

	return max


