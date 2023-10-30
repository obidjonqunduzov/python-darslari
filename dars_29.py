# Xatolar bilan ishlash 
# try harakat qilish
# try asosan xato yuz berishi mumkin bo'lgan qismiga ishlatiladi
# except aks holda,lekin degani


yosh = input("Yoshingizni kiriting: ")

try: # harakat shu kodni bajarishga harakat qiladi
	yosh = int(yosh)
	
except: # Xato yuzaga kelgan payt nima qilishni aytish pythonga
	print("Siz butun son kiritmadingiz!") # bu kodimiz toxtab qolmay kiyingi qismga o'tib ketadi
else:
	print(f" Siz {2023 - yosh} yilda tugilgansiz")



mevalar = ['uzum','olma','anor','nok']
try:
	print(mevalar[5])
except IndexError: # xatoni nomi
	print(f"Royxatimizda {len(mevalar)} ta meva bor xalos")



n = input("Butun son kiriting: ")
try:
	n = int(n)
	x = 20/n
except ValueError: # agar foydalanuvchi butun sin kiritmasa
	print("Butun son kiritmadingiz!")
except ZeroDivisionError: # agar foydalanuvchi 0 kiritsa
	print("0 ga bo'lin bo'lmaydi")
else:
	print(f"x={x}")


import json

filename = 'C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\json_fayl\\talaba_2.txt'
try:
	with open(filename) as f:
		text = f.read()
except FileNotFoundError:
	print(f"Uzur bizda {filename} fayli mavjud emas!")

files = [
'C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\json_fayl\\talaba.json',
'C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\json_fayl\\bemor.json']
for filename_2 in files:
	try:
		with open(filename_2) as f:
			bemor = json.load(f)
	except FileNotFoundError:
		print(f"{filename_2} bunday file mavjud emas") # xudi shu qismda agar kod bajarilishini istamasak (pass) operatoridan foydalanamiz
		# pass shunchaki hech narsa bajarmay kiyingi kodga o'tib ketadi
	else:
		print(f"{bemor['ismi']}")


while True:
	age = input("Yoshingizni kiriting: ")
	if age.isdigit():
		age = int(age)
		break
print(f"Siz {2023 - age} da tug'ilgansiz")