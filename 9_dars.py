# if , elif va else darsi davomi!

yosh = int(input("Yoshingiz nichida? "))

if yosh <= 4:
	print("Sizga kirish bepul")
elif yosh <= 12:
	print("Sizga kirish 5somon")
elif yosh <= 20:
	print("Sizga kirish 10somon")
else:
	print("Sizga kirish 20somon")


# if da or (yoki) qoshimchasi bor

kun = input("Bugun qaysi kun? ")

if kun.lower() == 'shanba' or kun.lower() =='yakshanba':
	print('Bugun dam olish kuni! ')
else:
	print('Bugun ish kuni ')

# if da and (va) qoshimchasi bor

kun_2 = input('Bugun qaysi kun? ')
harorat = float(input('Havo harorari qancha? '))

if kun_2.lower() == 'yakshanba' and harorat >= 30:
	print('Chomilgani ketdek! ')
elif kun_2.lower() == 'yakshanba' and harorat <=30:
	print('Uyda dam olamiz!')
else:
	print('Kunlardan birini kiriting!!! ')


# if da or va and operatorlaridan foydalanamiz!

kun_3 = input('Bugun qaysi kun? ')
harorat_2 = float(input('Havo harorari qancha? '))

if (kun_3.lower() == 'yakshanba'   or kun_3.lower() == 'shanba') and harorat_2 >= 30:
	print('Chomilgani ketdek! ')
elif (kun_3.lower() == 'yakshanba' or kun_3.lower() == 'shanba') and harorat_2 <=30:
	print('Uyda dam olamiz!')


narx = 15 
choy = True 	# yoki False
salat = False 	# yoki True

if choy and salat :
	narx = narx + 10
elif choy or salat :
	narx = narx + 5
print(f'Umumiy narx {narx} somon boldi!')

# bir necha if lardan foydalanamiz!
 # Boolean da True va False qiymatlarini orniga 1 va 0 dan foydalansak xam boladi! 

narx_2 = 10
choy_2 = True 	# yoki 1 va 0 dan xam foydalansak boladi!
salat_2 = True
non = False
asarti = True

# quyidagi aperator xar bir if ni aloxida-aloxida tekshiradi!

if choy: # agar olsa
	print('Mijoz choy oldi ')
	narx_2 = narx_2 + 3
if salat_2:
	print('Mijoz salat oldi ')
	narx_2 = narx_2 + 5
if non:
	print('Mijoz non oldi ')
	narx_2 = narx_2 + 4
if asarti:
	print('Mijoz asarti oldi ')
	narx_2 = narx_2 + 8

print(f'Umumiy narx {narx_2} boldi')
 
# if da yana in va not in operatorlari bor!

menu = ['osh', 'somsa', 'norin', 'shashlik']
zakaz = ['osh', 'norin', ' somsa']

if zakaz:
	for taom in zakaz:
		if taom in menu:
			print(f'Menuda {taom} bor')
		else:
			print(f'Kechirasiz , menuda {taom} yoq')
else:
	print('Savatcha bosh!!! ')