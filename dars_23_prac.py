# 23 dars buyicha uyga vazifa!


class Avto:
	def __init__(self,name,model,rang,karobka,narh,ish_davlat):
		self.name = name
		self.model = model
		self.rang = rang
		self.karobka = karobka
		self.narh = narh
		self.ish_davlat = ish_davlat
		self.ut_yuli = 10
		self.new_avto = []

	def get_info(self):
		"""Avtomobil haqida to'liq ma'lumot"""
		return f" {self.name.title()} avtomobili {self.ish_davlat.title()}da ishlab chiqarilgan,\n hozirda shu avtomobilning {self.model} modeli rangi {self.rang} va {self.karobka} karobka: {self.narh} $ , bosib otgan yoli {self.ut_yuli} km"

	def set_km(self,ut_yuli):
		"""Bosib otgan km yangilash"""
		self.ut_yuli = ut_yuli

	def update_km(self):
		"""Bosib utgan yo'lini xisoblash"""
		self.ut_yuli +=10

	def get_avto(self):
		return [km.get_info() for km in self.new_avto]

avto_1 = Avto('mersedes_benz','sls','qora','avtomat',25000,'germaniya')
avto_2 = Avto('range rover','optima','qora','avtomat',45000,'angliya')
avto_3 = Avto('tayota','prado','oq','mexanik',35000,'yaponiya')
avto_4 = Avto('haval','x7','qizil','avtomat',14000,'xitoy')

avto_1.update_km()
avto_1.update_km()
avto_1.update_km()
avto_1.update_km()
avto_1.update_km()

print(avto_1.get_info())

class New_avto:
	def __init__(self,salon):
		self.salon = salon
		self.yangi_avto = 0

	def add_avto(self,saln_avto):
		self.new_avto.append(saln_avto)	
		self.yangi_avto += 1

	def get_sal_avto(self):
		"""Sotuvdagi avtomobillar"""
		return [saln_avto.get_info() for saln_avto in self.new_avto]
	def get_apd_avto(self):
		return self.yangi_avto

sl_avtolar = New_avto("Orion Avto Saloni")
avto_1 = Avto('mersedes_benz','sls','qora','avtomat',25000,'germaniya')
avto_2 = Avto('range rover','optima','qora','avtomat',45000,'angliya')
avto_3 = Avto('tayota','prado','oq','mexanik',35000,'yaponiya')
avto_4 = Avto('haval','x7','qizil','avtomat',14000,'xitoy')
sl_avtolar.add_avto(avto_1)
sl_avtolar.add_avto(avto_2)
sl_avtolar.add_avto(avto_3)
sl_avtolar.add_avto(avto_4)

print(sl_avtolar.get_sal_avto())
