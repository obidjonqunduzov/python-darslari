# funksiya *args va *kwargs uzgaruvchan funksiyalar
# args funksiyasi istalgancha qiymat kiritsa boladi!

def summa(*sonlar): # *args ishorasi
	yigindi = 0
	for son in sonlar:
		yigindi += son
	return yigindi
print(summa(1,2))
print(summa(4,5,6,7)) # foydalanuvchi istalgancha qiymat kirita oladi!


#def qiymat(*sonlar):
	#return sum(sonlar)
#print(qiymat(1,5,8,9))

def qiymat(x,y,*sonlar):
	return x+y+sum(sonlar)
print(qiymat(4,2,5,6,4,))
print(qiymat(1,2))

# **kwargs (kalit sozli argument) dan foydalanamiz

def avto_info(kompaniya,model, **malumotlar):
	"""Avto haqidagi malumotlarni lugat korinishida qaytaruvchi funksiya"""
	malumotlar['kompaniya']=kompaniya
	malumotlar['model']=model
	return malumotlar

avto1 = avto_info("Opel","astra",rangi='qora', yil=2018)
avto2 = avto_info('Mersedes_benz','sls', rangi='oq',yili=2020, narxi=25000)

print(avto1)
print(avto2)

# Uyga vazifa

# 1

def son(*sonlar):
	return sum(sonlar)
print(son(1,2,3,4,5,6,7,8,9))

# 2 

def talabalar(ism,familiya,**boshqa_malumotlar):
	boshqa_malumotlar['ism']=ism
	boshqa_malumotlar['familiya']=familiya
	return boshqa_malumotlar
talaba_info=talabalar('Hasan','Mannonov',t_yili=1998,t_joyi='Tajikistan',kurs=4,fakultet='FizTex')
print(talaba_info)

# practika 1
# ixtiyoriy raqamlarni hisoblovchi dastur tuzamiz!


