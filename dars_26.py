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

avto_1 = Avto("Mersedes-Benz","sls","qora",2018,45000)
print(avto_1.get_avto_info())