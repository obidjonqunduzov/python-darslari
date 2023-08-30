# Xatolar bilan ishlash!

# print "Hello world" # xatolik () qolib ketdi

# print("Hello world" # xatolik EOF(qaysidir amalda qovus yopilmay qoldi) degani

# print("Hello world  # xato EOL(qaysidir amalda skobka yani "" yopilmay oldi ) degani

 #  print("Hello world") # xato bush joy qolib ketgan!	 

mevalar = ['olma', 'nok', 'anjir', 'qovun']
for meva in mevalar:
	print(meva)
	#print("Dastur tugadi! ") # xato yani bu amalni joy tashlamasdan yozish kerak edi!
print("Dastur tugadi! ") # mana bu amal togri!

# Uyga vazifa!

# 1

son = float(input("Juft son kiriting: "))
if son%2 == 1: # xato bor edi
	print("Bu juft son emas") # xato bor edi
else:
	print("Raxmat")

# 2
 
yosh = int(input("Yoshingizni nehida? ")) # xato bor edi

if yosh <= 4 or yosh >=60:
	narh = 0 # xatolik bor bu amal kerak emas!
	print("Sizga kirish bepul")
elif yosh < 18:
	narh = 10000
else:
	narh = 20000
	print(f'chipta {narh} som')

# 3

x = float(input("Borinchi sonni kiriting: ")) # xato bor edi
y = float(input("Ikkinchu sonni kiriting: ")) # xato bor edi

if x==y:
	print(f"{x} = {y}")
elif x<y:
	print(f"{x} < {y}") # xato bor edi
else: # xato bor edi
	print(f"{x} > {y}")

# 4

mahsulotlar = ['un','yog','sabzi','kartoshka']

savat = []
for n in range(5):
	savat.append(input(f"Savatga {n+1} mahsulotni qoshing: "))

if savat:
	for mahsulot in savat:
		if mahsulot in mahsulotlar:
			print(f"Dokonimizda {mahsulot} bor")
		else:
			print(f"Dokonimizda {mahsulot} yoq")
else:
	print("Savatchangiz bosh")