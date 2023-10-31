
# Json bilan tanishamiz!

import json

bemor = {
	'ismi':'Olim Olimov',
	'yoshi':26,
	'oila':True,
	'farzandlar':('Ifora'),
	'allergiya':None,
	'dorilar':[
		{'nomi':'Analgin','miqdori':0.5},
		{'nomi':'Panadol','miqdori':1.2}
	]
}

with open('C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\json_fayl\\bemor.json','w') as f:
    json.dump(bemor,f)

bemor_json = json.dumps(bemor, indent = 4)
print(bemor_json)

# json formatidan python formayiga o'tkazadi

filename = 'C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\json_fayl\\bemor.json'
with open(filename) as f:
    bemor = json.load(f)
    
print(type(bemor))

bemor2 = json.loads(bemor_json)
print(bemor2)

# Uyga fazifa

# 1

data = {
	"model":'opel',
	"rangi":"qora",
	"yili":2015,
	"narxi":8000
}
# data.json faylliga ushbu malumotlarni kiritamiz 

with open('C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\json_fayl\\data.json','w') as d:
	json.dump(data,d)

data_json = json.dumps(data,indent = 3)
print(data_json)



# 2

talaba = {
	"ismi":"sarvar",
	"familiyasi":"shodmonov",
	"kurs":3,
	"t_yili":2001
}
# talaba.json faylliga ushbu malumotlarni kiritamiz

with open('C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\json_fayl\\talaba.json', 'w') as t:
	json.dump(talaba, t)

talaba_json = json.dumps(talaba, indent = 3)
print(talaba_json)

# 3

# json formatini pythonga ogirib shu fayllar ustifa ishlash uchun

students = 'C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\json_fayl\\students.json'

with open(students ) as s:
	students = json.load(s)

print(f"{students} \n")

name = students['student'][0]['name']
kurs = students['student'][0]['year']
facultet = students['student'][0]['faculty']

print(f"ismi {name}, {kurs} kurs talabasi, {facultet} facultetida o'qiydi \n")

name = students['student'][1]['name']
kurs = students['student'][1]['year']
facultet = students['student'][1]['faculty']

print(f"ismi {name}, {kurs} kurs talabasi, {facultet} facultetida o'qiydi\n")
name = students['student'][2]['name']

kurs = students['student'][2]['year']
facultet = students['student'][2]['faculty']

print(f"ismi {name}, {kurs} kurs talabasi, {facultet} facultetida o'qiydi")