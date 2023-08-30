# raqamlar bilan ishlash!
# int-butun sonlar uchun, float-onlik sonlar uchun misol:(10.5)
# type sonlarni qaysi guruxga tegishli ekanligini korsatadi
# constanta-ozgarmas qiymat lekin pythonda katta harflar bilan yozsa (CONSTANTA)-boladi!

aholi_soni = 7_564_985
print(aholi_soni)

radius = 40
deametr = 2 * radius
PI = 3.14159

print("aylananing uzunligi=",deametr * PI)
type(deametr)

ism = 'Obidjon'
yoshi = 25
xabar = ism + ' ' + str(yoshi) + ' ' +  'yoshda'
print(xabar)

tugulgan_yil = int(input("tugilgan yilingizni kriting: "))
hozirgi_yil = 2023 - tugulgan_yil
print("Siz ",hozirgi_yil,"yoshda ekansiz!")


#uyga vazifa!
# 1
# istalgan qiymatni kvadartga va kubga kotarish

son_1 =int(input("biror son kiriting: "))

kvadrati = son_1 * son_1 
kubi = son_1 * son_1 * son_1
print("son kavadrati  ",kvadrati)
print("son kubi ",kubi)

#2
# istalgan insonni yoshini sorab tugilgan yilini aniqlash

yoshi = int(input("Yoshingizni kiritinh: "))
javob = 2023 - yoshi
print("Siz ",javob,"- yilda tugilgansiz!")

#3
# ikkita qiymat kiritish va uni + , - , * , / ammalarini xisoblash

qiymat_1 = int(input("birinchi qiymat "))
qiymat_2 = int(input("ikkinchi qiymat "))
javoblar_1 = qiymat_1 + qiymat_2
javoblar_2 = qiymat_1 - qiymat_2
javoblar_3 = qiymat_1 * qiymat_2
javoblar_4 = qiymat_1 / qiymat_2

print("umumiy natija qoshis: ",javoblar_1)
print("umumiy natija ayirish: ",javoblar_2)
print("umumiy natija kopaytirish: ",javoblar_3)
print("umumiy natija bolish: ",javoblar_4)


# shaxsiy practika


kun = int(input("tugulgan kuningizni kiriting: "))
oy = int(input("tugilgan oyingizni raqamini kiriting: "))
yil = int(input("tugilgan yilingizni kriting: "))
kun_javob = 31 - kun
oy_javob = 12 - oy
yil_javob = 2023 - yil

print("Siz ", yil_javob, "yosh ", oy_javob, "oylik" , kun_javob, "kunlik ekansiz!")

