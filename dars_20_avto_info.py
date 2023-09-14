# Modullar bilan tanishamiz



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


print("Saytimizda avtomobillar ruyxatini shakllantiramiz!")

def avto_kirit():
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
	return avtolar
	print("Salondagi avtomoshinalar: ")

def info_print(avto_info):
	for avto in avtolar:
		if avto['narh']:
			narh = avto['narh']
		else:
			narh = 'Nomalum'
			print(f"{avto['rangi'].title()} {avto['model'].title()} {avto['karobka']} karobka, Narh: {narh}")