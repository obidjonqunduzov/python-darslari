# for(uchun) ciklidan foydalanamiz!

mexmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Doston']

for mexmon in mexmonlar:
	print("Salom ", mexmon)
	print(f'Hurmatli {mexmon}, sizlarni 10-oktyabrga oshga taklif qilaman!')
	print('Hurmat bilan, Qunduzovlar oilasi')
# bu dastur bir xel ammalarni bajarish uchun foydalaniladi, yani xar biriga aloxida print() deb cgiqarmasdan bittada shu dasturdan foydalanamiz!

sonlar = list(range(1,11))

for son in sonlar:
	print(f'{son} ning kvadrati {son**2}ga teng')

####################################

sonlar_2 = list(range(11))
sonlar_kvadrati = []

for son_2 in sonlar_2:
	sonlar_kvadrati.append(son_2**3)

####################################


print(sonlar_kvadrati)
print(sonlar_2)

kara_jadval = list(range(1,11))
t = 9
for kara in kara_jadval:
	print(f'{kara} x {t} = {kara *t}')

######################################

dostlar = []

print('Eng yaqin 3 ta dustingizni ismini kiriting: ')

for n in range(3):
	dostlar.append(input(f'{n+1}) dostingizni ismini kiriting : '))
print(dostlar)


# Uyga vazifa!

# 1
ismlar = ['Bexzod', 'Bobir', 'Oxunjon', 'Komiljon', 'Olimjon']

for ism in ismlar:
	print(f'Hurmatli {ism} 5-sentyabrda Bexzodlarnikiga naxorga!')
	print(f'kod {len(ismlar)} takrorlandi')

# 2

raqamlar = list(range(10,100,3))

for raqam in raqamlar:
 	print(f'{raqam} x {raqam} = {raqam**3}')

# 3

filmlar = []
for n in range(3):
	filmlar.append(input(f'{n+1} eng sevimli kinolaringiz!: '))
print(filmlar)

# 4

suhbatlar = []
print('Bugun kimlar bilan suhbatlashdingiz? ')

for n in range(4):
	suhbatlar.append(input(f'{n+1} -suhbat qilgan odamim !'))
print(suhbatlar)
