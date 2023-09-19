# Soz topish oyini

import  random

	

	
son_x = 10
print(f"Men 1 dan {son_x} son oylayman siz uni toping")
tasodifiy_son = random.randint(1,son_x)
taxminlar_ins = 0
kompyuter = True
while kompyuter:
	taxminlar_ins +=1
	son_krit = int(input(f"Uzingizni {taxminlar_ins} chi taxminiy soningizni kriting: "))
	if son_krit < tasodifiy_son:
		print("Xato! Harakat qiling men oylagan son bundan katta")
	elif son_krit > tasodifiy_son:
		print("Xato! Harakat qiling men oylagan son bundan kichik")
	else:
		print("Topdingiz men shu sonni oylagan edim!")
		break

print(f"Siz men oylagan sonni {taxminlar_ins} urunishda topdingiz \n")

input(f"Endi siz 1 dan {son_x} oylang men uni topishga harakat qilaman! ")
	
quyi = 1
yuqori = son_x
taxminlar_kom = 0
inson = True
while inson:
	taxminlar_kom +=1
	if quyi != yuqori:
		tasodifiy_son = random.randint(quyi,yuqori)
	else:
		tasodifiy_son = quyi
	javob = input(f"Siz {tasodifiy_son} sonini oyladingiz: togri(t): ,"
		f"men oylagan son bundan kattaroq (+): , yoki kichikroq (-): ")

	if javob =='-':
		yuqori = tasodifiy_son - 1
	elif javob == '+':
		quyi = tasodifiy_son + 1
	else:
		break
	
print(f"Men {taxminlar_kom} da topdim! ")


taqqoslash = True
while taqqoslash:
	if taxminlar_kom > taxminlar_ins:
		print(f"Siz yutdingiz")
	elif taxminlar_kom < taxminlar_ins:
		print(f"Men yutdim")
	else:
		print("Durrang")
		break
	taqqoslash = int(input("Yana oynamizmi ha (1) / Yoq (0) : "))






