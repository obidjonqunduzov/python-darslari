#string (str)-dan foydalanzmiz!

ism = "Obidjon"
familiya = "Qunduzov"
shahar = "Худжанд"
print(ism,familiya,shahar)

#Unicode saytidan foydalaning!

print(ism + ' ' + familiya)

ism_2 = "Ahad"
familiya_2 = "Yunusov"

# upper() hamma harflarni kattalashtiradi

ism_sharif = f"{ism_2} {familiya_2}"
print(ism_sharif.upper())

ism_3 = 'Bond'
familiya_3 = 'James'
print(f'Mening ismim {ism_3}.{ism_3} {familiya_3}')


# \t katta bushliq qoldiradi
# \n  qatorga bulish

# lstrp() katta bushliqlarni chap tomonini kamaytiradi
# rstrip() katta bushliqlarni ung tomondan kamaytiradi
# strip() har ikki tomondan kamaytiradi

meva = '    olma   '
print("men" + meva.lstrip() + "yaxshi koraman")

# uyga vazifa shularni bitta kurinishda chiqarish!

kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor" 
viloyat="Samarqand"

natija = (f"{kocha} kochasi, {mahalla} mahallasi, tumani {tuman}, {viloyat} viloyati")
print(natija.upper(), kocha.lower())