
# class dan foydalanamiz!

class Talaba:
	def __init__(self,ism,familiya,t_yili):
		self.ism = ism
		self.familiya = familiya
		self.t_yili = t_yili

	def tanishuv(self):
		return f" Ismim {self.ism} {self.familiya} tugilgan yilim {self.t_yili} "

	def get_name(self):
		return self.ism	

	def get_yosh(self,hozirgi_yil):
		return hozirgi_yil - self.t_yili



talaba1 = Talaba("Olim","olimov",2001)
talaba2 = Talaba("obidjon","Qunduzov",1998)
print(talaba2.tanishuv())

# Uyga vazifa

# 1

class User:
	def __init__(self,name,last_name,age,phone_number,email):
		self.name = name
		self.last_name = last_name
		self.age = age
		self.email = email
		self.phone_number = phone_number
		

	def age_info(self,yoshim):

		return f" Mening ismim {self.name.title()} {self.last_name.title()} yoshim {yoshim - self.age} da, telefon nomerim: {self.phone_number} email pochta manzilim: {self.email} "

	def otam(self,yoshlari):
		return f" Otamning ismlari {self.name.title()} yoshlari {yoshlari - self.age} da"
		

user_otam = User('komiljon','qunduzov',1976,89916254113,'obidjon@gmail98.com')
print(user_otam.otam(2023))


user_info = User(' obidjon','qunduzov',1998,89916254113,'obidjon@gmail98.com')
print(user_info.age_info(2023))


