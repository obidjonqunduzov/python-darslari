# Soz topish oyini

import  random

def sontop(x=10):
	tasodifiy_son = random.randint(1,x)
	print(f"Men 1 dan {x} gacha son oylayman, Siz topasiz")
	taxminlar = 0

	while True:
		taxminlar +=1
		taxmin = int(input(">>>"))
		if taxmin<tasodifiy_son:
			print("Xato! Men oylagan son bundan katta.Harakat qiling")
		elif taxmin>tasodifiy_son:
			print("Xato! Men oylagan son bundan kichik.Harakat qiling")
		else:
			break
	print(f"Tabriklaymiz. {taxminlar} va txmin bilan topdingiz")	

	
