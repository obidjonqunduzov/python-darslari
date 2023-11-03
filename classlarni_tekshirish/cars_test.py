import unittest
from cars import Car

class CarTest(unittest.TestCase):
	"""Car classini tekshiradi"""

	def setUp(self):
		make = "Mersedes-Benz"
		made = "SLS"
		year = 2020
		self.price = 75000
		self.km = 10000
		self.avto_1 = Car(make,made,year)
		self.avto_2 = Car(make,made,year,price=self.price)

		# E'tibor bering, setUp() metodi ichida ba'zi o'zagruvchilar 
		# self yordamida berilgan (self.price,self.km, self.avto1, self,avto2). 
		# Bu o'zgaruvchilarga biz CarTest() klassining ichida istalgan joydan murojat qilishimiz mumkin. 
		# Shuning uchun ham, test_create() funksiyasi ichida biz yangi obyekt yaratmasdan, 
		# setUp() ichidagi avto1 va avto2 obyektlariga murojat qildik.

	def test_creative(self):
		# avto_1 ga km va narhini bermay tekshiramiz
		avto_1 = Car("tayota","camry",2018)

		# Qiymat mavjudligini assertIsNotNone() metodi bilan tekshiramiz

		self.assertIsNotNone(avto_1.make)
		self.assertIsNotNone(avto_1.made)
		self.assertIsNotNone(avto_1.year)

		# Qiymat mavjud emasligini assertIsnone() metodi bilan tekshiramiz

		self.assertIsNone(avto_1.price)

		# Qiymat tengligini assertEqual() metodi bilan tekshiramiz

		self.assertEqual(0,avto_1.get_km())

		# Yangi obyekt yaratamiz va unda narhini ham beramiz

		# avto_2 = Car("tayota","camry",2018,price = 55000)
		# self.assertEqual(55000,avto_2.price)

	def test_set_price(self): # narxini tekshiruvchi test
		new_price = 55000
		self.avto_2.set_price(new_price)
		self.assertEqual(new_price, self.avto_2.price)

	def test_add_km(self):
		# Musbat qiymat berib ko'ramiz
		self.avto_1.add_km(self.km)
		self.assertEqual(self.km, self.avto_1.get_km())
		
		# Manfiy qiymat berib ko'ramiz

		new_km = -4000
		try:
			self.avto_1.add_km(new_km)
		except ValueError as error:
			self.assertEqual(type(error), ValueError)
		
	

     



unittest.main()