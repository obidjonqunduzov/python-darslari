# Soz topish oyini

import random as ran

print("Keling soz topish oyinini oynaymiz! ")

n = 1


while True:
	son = ran.sample(range(10),1)
	savol =f"1 dan 10 gacha son oyladim uni toping {n}: "
	soz_kiritish = int(input(savol))
	
	n +=1


	if soz_kiritish < son:
		print("Harakat qiling, men oylagan son bundan kichik")
	elif soz_kiritish  > son:
		print("Men oylagan son bundan katta")
	else:
		
		print("topdingiz! ")

	#for topdi in savol:
		#print(f"Siz {n} da topdingiz")
	#print("Yana oynaymizmi?")

	
