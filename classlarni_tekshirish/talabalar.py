# Voris class bilan tanishamiz!

class Shaxs:
	def __init__(self,name,lastname,age,professiy):
		self.name = name
		self.lastname = lastname
		self.age = age
		self.professiy = professiy

	def get_info(self):
		return f"{self.name.title()} {self.lastname.title()} , was born in Tajikistan he has  {2021 - self.age}, he a {self.professiy} in school "




class Student(Shaxs): # Shaxs classining vorisi Talaba classi bo'ladi!
	def __init__(self,name,lastname,age,professiy,facultet,uneversity,live):
		super().__init__(name,lastname,age,professiy)
		self.facultet = facultet
		self.uneversity = uneversity
		self.live = live

	def get_uneversity(self):
		return self.uneversity

	def get_facultet(self):

		return self.facultet

	def get_info(self):
		return  f"{self.name.title()} {self.lastname.title()} , was born in Tajikistan he has  {2021 - self.age}, he a {self.professiy} in school, he read on {self.facultet} on uneversity of {self.uneversity}"




class Live:
	"""Talabaning yashash joyini qaytaradi"""
	def __init__(self, street,city,region):
		self.street = street
		self.city = city
		self.region = region

	def get_info_live(self):
		return f"{student_1.get_info()},he live in  {self.region.title()}, {self.city.title()}, {self.street.title()}"






student_live = Live("f.otakhonov 47","khujand","sugd")
student_1 = Student("obidjon","qunduzov",1997,"teacher2","fiztex","HGU",student_live)

print(student_1.live.get_info_live())