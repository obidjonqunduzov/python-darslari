# xatolar bilan ishlash classlarni tikshirish

class Car():
	def __init__(self,make,made,year,price=None,km=0):
		self.make = make
		self.made = made
		self.year = year
		self.price = price
		self.__km = km

	def set_price(self,price):
		self.price = price

	def add_km(self,km):
		"""Mashinani km kopaytiradi"""
		if km>=0:
			self.__km += km
		else:
			raise ValueError("Km manfiy bo'lishi mumkin emas!")

	def get_km(self):
		return self.__km

	def get_info(self):
		info = f"{self.make.upper()}, {self.make.title()},"
		info += f"{self.year} - yil, {self.__km} km yurgan"
		if self.price:
			info += f"Narhi: {self.price}"

		return info
