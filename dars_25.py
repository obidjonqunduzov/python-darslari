
# OOD . Inkapsulatsiya bilan tanishamiz!

from uuid import uuid4

class Book:
	""" Book classi """
	def __init__(self,name_bk,payge,price,discount=0):
		self.name_bk = name_bk
		self.payge = payge
		self.price = price
		self.__discount = discount
		self.__id = uuid4()

	def get_discount(self):
		return self.__discount

	def get_id(self):
		return self.__id

	def add_discount(self,discount):
		"""Chegirmani kopaytiradi"""
		if discount >= 0:
			self.__discount += discount
		else:
			print("Cegirmani kamatirib bo'lmaydi!")

	def get_book_info(self):

		book = f"{self.name_bk.title()} nomli kitob, {self.payge} sahifa, {self.price} $"
		return book
	def get_id_book(self):
		return f"{read_book.get_book_info()} kitobini dokonimizdan {read_book.get_discount()} % chegirma orqali xarid qilishingiz mumkin! ID {read_book.get_id()}"

read_book = Book("Amallar niyatga bog'liq", 180, 7,15)
read_book.add_discount(15)
print(read_book.get_id_book())