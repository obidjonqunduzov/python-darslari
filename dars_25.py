
# OOD . Inkapsulatsiya bilan tanishamiz!
# __bu degani inkapulatsiya qilingan degani

from uuid import uuid4

class Book:
	""" Book classi """
	__num_book = 0
	def __init__(self,name_bk,payge,price,discount=0):
		self.name_bk = name_bk
		self.payge = payge
		self.price = price
		self.__discount = discount # bu yashirin, tahqaridan murojat qiqib bo'lmaydi!
		self.__id = uuid4()
		Book.__num_book += 1

	@classmethod
	def get_num_book(cls):
		return cls.__num_book

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
		return f"{self.get_book_info()} kitobini dokonimizdan\n {self.get_discount()} % chegirma orqali xarid qilishingiz mumkin! ID {self.get_id()}"

# davomi dars_25_next.py faylida saqlanyapdi