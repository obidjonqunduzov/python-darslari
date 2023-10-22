# class davomi

class Talaba:
	def __init__(self,ism,familiya,t_yili):
		self.ism = ism
		self.familiya = familiya
		self.t_yili = t_yili
		self.kurs = 1

talaba1 = Talaba('olim','olimov',1997)

print(talaba1.ism)

# bu unchalik tugri metod emas!
# buning oson yuli bor

class Talaba:
	def __init__(self,ism,familiya,t_yili):
		self.ism = ism
		self.familiya = familiya
		self.t_yili = t_yili
		self.kurs = 1
	def get_info(self):
		return f"{self.ism.title()} {self.familiya.title()} FizTex fakultetining {self.kurs} kurs talabasi"

	def get_name(self):
		"""Talabaning ismini qaytaradi"""
		return self.ism
	def get_lastname(self):
		"""Talabaning familiyasini qaytaradi"""
		return self.familiya
	def set_age(self):
		"""Talabaning yoshini qaytaradi"""
		return f" Talabaning yoshi {2023-self.t_yili}"
	def set_kurs(self):
		"""Talabaning nechanchi kurs ekanligini qaytaradi"""
		return self.kurs

talaba1 = Talaba('olim','olimov',1997)
talaba2 = Talaba('behzod','salimjonov',1998)
talaba3 = Talaba('bakhodir','abdulhakimov',1998)
talaba4 = Talaba('obidjon','Qunduzov',1998)
talaba5 = Talaba('abduroziq','majidov',1998)

print(talaba2.get_info())

# get (qoshish uchun) set (ozgartirish) uchun

class Fan():
	"""Fan nomli klass"""
	def __init__(self,nomi):
		self.nomi = nomi
		self.talabalar_soni = 0
		self.talabalar = []

	def get_name(self):
		"""Fan nomi"""
		return self.nomi

	def add_students(self,talaba):
		"""Fanga talabalarni qoshih"""
		self.talabalar.append(talaba)
		self.talabalar_soni += 1
		

	def get_students(self):
		"""Fanga yozilgan talabalar soni"""
		return [talaba.get_info() for talaba in self.talabalar]

	def get_students_num(self):
		"""Fanga yozilgan talabalar"""
		return self.talabalar_soni

	#def see_methods(klass):
  	  #	return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(Talaba))


fizika = Fan('Fizika va Texnika')

talaba1 = Talaba('olim','olimov',1997)
talaba2 = Talaba('behzod','salimjonov',1998)
talaba3 = Talaba('bakhodir','abdulhakimov',1998)
talaba4 = Talaba('obidjon','Qunduzov',1998)
talaba5 = Talaba('abduroziq','majidov',1998)

fizika.add_students(talaba1)
fizika.add_students(talaba2)
fizika.add_students(talaba3)
fizika.add_students(talaba4)

print(fizika.get_name())
print(fizika.get_students())
print(fizika.get_students_num())
print(fizika.see_methods(Talaba)