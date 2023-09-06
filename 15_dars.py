# while darsini davomi!
print("Doslaringiz royxatini tuzing!")
ismlar = []
n = 1
while True:
	savol = f"{n} dostlaringiz ismini kiriting: "
	ism = input(savol)
	ismlar.append(ism)
	takrorlash = input("Yana dostlaringizni qoshasizmi?  (ha/yoq) ")
	n += 1
	if takrorlash != 'ha':
		break


dostlar = {}
ishora = True

while ishora:
	ism = input("Dostlaringizni ismini kiriting: ")
	yosh = input(f"{ism.title()} ning yoshini kiriting: ")
	dostlar[ism] = int(yosh)

	javob = input("Yana malumot qoshasizmi? (ha/yoq) : ")
	if javob == 'yoq':
		ishora = False

for ism,yosh in dostlar.items():
	print(f"{ism.title()}  {yosh}  yoshda")

cars = ['mers','opel','tayota','opel','ferrari','rols-roys']
car = 'opel'
while car in cars:
	cars.remove('opel')
	print(cars)


talabalar = ['hasan','husan','botir','akmal']
baholangan_talabalar = {}
while talabalar:
	talaba = talabalar.pop()
	baho = input(f"{talaba.title()} ning bahosini kiriting: ")
	print(f"{talaba.title()} baholandi! ")

	baholangan_talabalar[talaba] = int(baho)

for talaba,talabalar in baholangan_talabalar.items():
	print(f"{talaba.title()} ning bahosi {talabalar} \n")


# Uyga vazifa

# 1


byurtma = []
byurtmalar_soni = 1
while True:
	soni = f"{byurtmalar_soni} byurtma nomini kiriting: "
	by_kritish = input(soni)
	byurtma.append(by_kritish)
	yana_byurtma = input("Yana byurtma kiritasizmi? aks holda(ha/yoq) : ")
	byurtmalar_soni +=1

	if yana_byurtma != 'ha':
	 break 
print(f"{byurtma} quyidagi byurtmalarni tanladingiz")

# 2

bozor = {}

narsalar = True
while narsalar:
	olmoqchi_b_narsalarimiz = input("Nimalar xarid qilmoqchi siz? : ")
	narxi = input("Necha pulga olmoqchi siz? : ")

	bozor[olmoqchi_b_narsalarimiz] = int(narxi)

	yana_olasizmi = input("Yana biror narsa xarid qilasizmi? (ha/yoq)")

	if yana_olasizmi == 'yoq':
		narsalar = False

	for olmoqchi_b_narsalarimiz,narxi in bozor.items():
		print(f"Siz {olmoqchi_b_narsalarimiz} xaridlaringiz {narxi}\n")

# 3

while byurtma:
	umumiy = byurtma.pop()
	if umumiy in bozor.keys():
		narxlar = bozor[olmoqchi_b_narsalarimiz]
		print(f"{umumiy} - {narxlar} somon")
	else:
		print(f"{umumiy} bizda bu narsa yoq! ")