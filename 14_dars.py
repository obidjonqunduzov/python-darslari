# while (toki) tsiklidan foydalanamiz!

son = 1
while son <=5:
	print(son, end=' ')
	son = son + 1
print(" dastur tugadi")


# sonlarni kvadratini hisoblobchi dastur!

#savol = 'istalgan sonni kiriting '
#savol += "( dasturni toxtatish uchun 'exit' deb yozing):  "
#qiymat = ''

#while qiymat != 'exit': # bu operatorni break (kesish) yordamida toxtatsak ham boladi!
	#qiymat = input(savol)
	#if qiymat != 'exit':
		#print(float(qiymat)**2)
#print("Dastur tugadi!")

sonlar = list(range(1,11))

for son_2 in sonlar:
	if son_2 == 8:
		break # continue        # bu operator amalni davom ettiradi 8ni qoshmaydi
	print(f"{son_2} ning kvadrati {son_2**2} ga teng")

son_3 = 0
while son_3 < 10:
	son_3 += 1
	if son_3 % 2 != 0: # == yozsak faqat toq sonlarni chiqaradi
		continue
	else:
		print(son_3)

	#son_3 += 1 bunday qilish xato , bunda cheksiz tsikl bolib qoladi!

# Uyga vazifa

# 1

sev_kitoblar = ("Yahshi korgan kitoblaringizni kiriting  ")

kitob_soni = ''

while kitob_soni != 'stop':
	kitob_soni = input(sev_kitoblar)
	if kitob_soni != 'stop':
		print(kitob_soni)
		print(" Dasturni toxtatish uchun 'stop' deb yozing: ")

print("Dastur tugadi")

# 2

print("Salom")

ism = input("Ismingizni kiriting: ")
qiymatlar = ''
while True:

    if qiymatlar == 'exit' or qiymatlar == 'boldi':
        break

    qiymat = (int(input("Yoshingizni kiriting: ")))

    yosh = qiymat

    if yosh <= 7:
        narh = 2
    elif 7 <= yosh < 18:
        narh = 5
    elif 18 <= yosh < 65:
        narh = 10
    else: narh = 0
    
    if narh==0:
        print(f"Hurmatli {ism.title()} sizga chipta bepul")
    else:
        print(f"Hurmatli {ism.title()} sizga chipta {narh} somon")
    print("Dastur toxtatish uchun 'exit' yoki 'boldi' yozing")
print("Dastur tugadi")