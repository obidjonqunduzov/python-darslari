# NESTING (lugat ichidagi bolimlar) bilan tanishamz!

car_1 = {
	'model':'tesla',
	'yili':2020,
	'narxi':120000,
	'turi':'elektrocar'
}

car_2 = {
	'model':'opel',
	'yili':2015,
	'narxi':55000,
	'turi':'mexanik'
}

car_3 = {
	'model':'mesedes-benz',
	'yili':2019,
	'narxi':110000,
	'turi':'avtomat'
}

cars =[car_1, car_2, car_3]

for car in cars:
	print(f"{car['model'].title()}",
		 f"{car['yili']} yili",
		 f"{car['turi']}, {car['narxi']} $")



avto_none = []
for n in range(5):
	new_car = {
		'model':'mesedes-benz',
		'yili':2019,
		'narxi':None,
		'turi':None,
		'rangi':None, # rangi noaniq
		'km':0
		}
	avto_none.append(new_car)

#for avto in avto_none:
	#print(avto)

for avto in avto_none[:2]:
	avto['rangi']='qora'

#for avto in avto_none:
#	print(avto)

for avto in avto_none[0:3]:
	avto['turi']='avtomat'

#for avto in avto_none:
#	print(avto)

for avto in avto_none[3:6]:
	avto['turi']='mexanik'

#for avto in avto_none:
#	print(avto)

for avto in avto_none:
	if avto['turi'] =="avtomat":
		avto['narxi']=40000
	else:
		avto['narxi']=35000
for avto in avto_none:
	print(avto)

dasturchilar ={
	'ali':['python','c++'],
	'vali':['html','css'],
	'hasan':['c#','js'],
	'obid':['php','sql']
}

for ism,tillar in dasturchilar.items():
	print(f"\n {ism.title()} quyidagi dasturlash tillarini biladi: ")
	for til in tillar:
		print(f'{til.upper()}', end=' ')

hamkasblar = {

	'bahzod':{
		'familiya':'salimjonov',
		't_yili':1998,
		'tillar':['python','c#']
	},
	'bahodir':{
		'familiya':'abdullahakimov',
		't_yili':1998,
		'tillar':['html','css','php']
	},
	'abduroziq':{
		'familiya':'majidov',
		't_yili':1998,
		'tillar':['c++','sql']
	},
	'obidjon':{
		'familiya':'qunduzov',
		't_yili':1998,
		'tillar':['python','c#','html css']
	}
}

for name,info in hamkasblar.items():
	print(f"\n {name.title()} {info['familiya'].title()},"
		f"{info['t_yili']} - yilda tugilgan.\n"
		f"quyidagi dasturlash tillarini biladi: ")
	for professiya in info['tillar']:
		print(f"{professiya.upper()}", end = ' ')



# Uyga vazifa

# 1

buyuklar = {

	'ismoil':{
	'ismi':' al buhoriy',
	't_sanasi':810,
	'ilmi':'hadis olimi',
	'asarlari':['al-jomius','al-adabul mufrad','kitobul favoid']
	},

	'stev':{
	'ismi':'jobs',
	't_sanasi':1952,
	'ilmi':'ixtirochi',
	'asarlari':['stev jobs']
	},

	'alisher':{
	'ismi':'navoiy',
	't_sanasi':1441,
	'ilmi':'shoir',
	'asarlari':['holoti pahlavon','navodir un-nihoya','naxmul javohir']
	},

	'amir':{
	'ismi':'temur',
	't_sanasi':1336,
	'ilmi':'sarkarda',
	'asarlari':['amir temur','temurlan']
	}

}

for ismlar,malumotlar in buyuklar.items():
	print(f"\n {ismlar.title()} {malumotlar['ismi'].title()},"
		f"{malumotlar['t_sanasi']} - yilda tavallud topgan",
		f"{malumotlar['ilmi']} bolib butun dunyoga tanilgan va quyidagi asarlarni yozgan: ",)

	for kitoblari in malumotlar['asarlari']:
		print(f"{kitoblari.title()}")
		



