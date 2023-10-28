
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


filename = 'C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\json_fayl\\bemor.json'
with open(filename) as f:
    bemor = json.load(f)
    
print(type(bemor))

bemor2 = json.loads(bemor_json)
print(bemor2)