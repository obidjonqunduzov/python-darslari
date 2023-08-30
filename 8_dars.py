# if va else bilan tanishamiz!

avtolar = ['mers', 'opel', 'bmw', 'volvo']

for avto in avtolar:
	if avto == 'bmw':
		print(avto.upper())
	else:
		print(avto.title())

# matnlar bilan ishlayotganda xamma matni bir xel korinishga keltirib olish kerak,
# yani katta xarf bilan yozilganlarni lower() yordamida bir xel kichik korinishga keltirish lozim!

# == bu teng degani
# != bu teng emasmi? degani

ism = input("Ismingizni kiriting:  ")
if ism.lower() != 'ali':
	print(f'Uzur {ism.title()} , biz Alini kutyapmiz! ')
else:
	print('salom Ali')

son = float(input('12 x 6 necgiga teng?' ))
if son != 72:
 	print('Xato')
else:
 	print('Togri javob')

yosh = int(input("yoshingizni kiriting: "))

if yosh >= 18:
	print('Xush kelibsiz!')
else:
	print('Kirish mumkin emas!!!')

login = input("yangi login tanlang: ")

if len(login) <= 5:
	print('Login 5 ta harfdan kop bolishi shart!!!')

yil = int(input("Tugilgan yilingizni kiriting:  "))

if (2023 - yil) <= 18:
	print(f'Yoshingiz {2023 - yil} ekan')
	print('Sizga kirish mumkin emas!')
else:
	print('Xush kelibsiz!')

yosh_2 = int(input("Yoshingizni kiriting: "))

if yosh_2 > 65: print('Siz covid-19 risk guruhudasiz!')

x,y =50, 30
print('x > y') if x > y else print('x < y')

# Uyga vazifa!

# 1

cars = ['tayota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
	if car == 'gm':
		print(car.upper())
	else:
		print(car.title())

# 2
cars = ['tayota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
	if car != 'gm':
		print(car.upper())
	else:
		print(car.title())

# 3
foydalanuvchi = input('Loginingizni kiriting: ')
if foydalanuvchi == 'admin':
	print('foydalanuvchilar royxatini korasizmi?')
else:
	print('{foydalanuvchi ismi}!')

# 4
qiymat = int(input("Istalgan son kiriting: "))
if qiymat >= 1:
	print('Musbat son!')
else:
	print('Manfiy son!!!')

	