# Voris class bilan tanishamiz!

class Shaxs:
	def __init__(self,name,lastname,age,professiy):
		self.name = name
		self.lastname = lastname
		self.age = age
		self.professiy = professiy

	def get_info(self):
		return f"{self.name.title()} {self.lastname.title()} , was born in Tajikistan he has  {2021 - self.age}, he a {self.professiy} in school "

info = Shaxs("Obidjon","Qunduzov",1998,"teacher")
print(info.get_info())

class Student(Shaxs): # Shaxs classining vorisi Talaba classi bo'ladi!
	def __init__(self,name,lastname,age,professiy,facultet,uneversity):
		super().__init__(name,lastname,age,professiy)
		self.facultet = facultet
		self.uneversity = uneversity

	def get_uneversity(self):
		return self.uneversity

	def get_facultet(self):
		return self.facultet



student_1 = Student("obidjon","qunduzov",1997,"teacher2","fiztex","HGU")

print(f"{student_1.get_info()}, he read on {student_1.get_facultet()} on uneversity of {student_1.get_uneversity()}")