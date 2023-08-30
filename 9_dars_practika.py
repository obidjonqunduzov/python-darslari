# Uyga vazifa
# 1

qiymat = int(input("Juft son kiriting: "))

# %2 bu toq son degani!
if qiymat%2:
	print('Juft son kiriting')
else:
	print('Raxmat')


# 2

yosh = int(input("Yoshingiz nichida? "))

if yosh <= 6 or yosh >= 60:
	print('Sizga kirish bepul')
elif yosh <= 18:
	print('Sizga kirish 10 somon')
elif yosh >= 20:
	print('Sizga kirish 20 somon')
else:
	print('Yoshingizni kiriting!!!')

# 3

son = float(input("birinchi sonni kiriting: "))
son_2 = float(input("ikkinchi sonni kiriting: "))

if son > son_2:
	print(f'bu sonlar {son} > {son_2} ')
elif son < son_2:
	print(f'bi sonlar {son} < {son_2}') 
elif son == son_2:
	print(f'bu sonlar {son} = {son_2}')

# 4

mahsulotlar = ['uzum', 'anor', 'gilos', 'olma', 'urik', 'shaftoli', 'anjir']

savat = []

for n in range(5):
	savat.append(input(f'Svatga {n+1} mahsulotni qoshing: '))

for mahsulot in savat:
	if mahsulot in mahsulotlar:
		print(f'Dokonimizda {mahsulot} bor')
	else:
		print(f'Dokonimizda {mahsulot} yoq')

# 5

foydalanuvchilar = ['olimjon@gmail', 'obidjon@gmail', 'Komiljon@gmail']

foydalanuvchi = input("Yangi login kiriting: ")

if foydalanuvchi in foydalanuvchilar:
	print('Bu login bant')
else:
	print(f'Xush kelibsiz {foydalanuvchi.title()}')

# 6

butun_son = int(input("butun son kiriting: "))

for s in range(1,11):
	if not (butun_son%s):
		print(f'{butun_son} soni {s} ga qoldiqsiz bolinadi!')





