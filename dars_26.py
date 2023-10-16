# Dunder metodhi bilan tanishamiz!

class Avto:
	#__num_avto = 0
 	def __init__(self,firma,model,rangi,yili,narxi):
 		"""Avtomobilning xsusiyatlari"""
 		self.firma = firma
 		self.model = model
 		self.rangi = rangi
 		self.yili = yili
 		self.narxi = narxi
 		#Avto.__num_avto += 1

 	def get_avto_info(self):
 		return f"{self.firma} {self.model},{self.rangi},{self.yili},{self.narxi}"

 	def __repr__(self):
 		return f"Avto: {self.firma} {self.model}" # tushunarsiz obyekt matnini tushunarli qiladi

 	# biz kritgan malumotlarni bir biri bilan solishtirish uchun quyidagi operatordan foydalanamiz!

 	def __eq__(self,y): # self(birinchi avto) y(ikkinchi avto)
 		return self.narxi == y.narxi # ikkisi teng yoki yoq shuni ko'rsatadi

 	def __lt__(self,y):
 		return self.narxi < y.narxi # katta yoki kischik shuni ko'rsatadi

 	def __le__(self,y):
 		return self.narxi <= y.narxi # katta kichik yoki teng shuni ko'rsatadi

avto_1 = Avto("Mersedes-Benz","sls","qora",2018,45000)
avto_2 = Avto("Opel","atra","oq",2005,5000)


class AvtoSalon:
	def __init__(self,name):
		self.name = name
		self.avtolar = []

	def __repr__(self):
		return f"{self.name} avto saloni"

	def __getitem__(self,index):
		return self.avtolar[index]

	def add_avto(self,*qiymat):
		for avto in qiymat:
			if isinstance(avto,Avto):
				self.avtolar.append(avto)
			else:
				print("Avto kiriting!")


salon_1 =AvtoSalon("Orion Avto")

salon_1.add_avto(avto_1,avto_2)

print(salon_1[:])