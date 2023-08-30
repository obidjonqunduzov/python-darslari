# List[] bilan tanishamiz!

mevalar = ['olma', 'nok', 'shaftoli', 'banan']
son = [54, 65, 25, 89]
aralash = ['bir', 'ikki', 3, 4, 5]
print(mevalar)
print(son)
print(aralash)
# listda sanaganda 0 dan boshlab sanaymiz!
# list -1dan xam foydalansa boladi!

#listni ichidagi sozni almashtirish!

mevalar[-2] = 'orik'
print(mevalar)

# listni ohiriga qiymat qoshish append() yordamida qoshamiz!

mevalar.append('angir')
print(mevalar)

# listni istalgan joyiga insert() orqali qiymat qushamiz!

mevalar.insert(1, 'uzum')
print(mevalar)

# listni ichidagi istalgan qiymatni  del() orqali uchiramiz!

del mevalar[0]
print(mevalar)

# listdagi qiymatlar uzun ulardagi bitta qiymatni uchurish uchun uning indexsini bilmaymiz uni remove() orqali uchiramiz!
# remove() faqat list ichidagi birinchi qiymatni uchiradi agar qiymatlar bittadan kop bolsa uni yana ishlatamiz!

mevalar.remove('banan')
print(mevalar)

# listni ichidagi biror qiymatni yulib olish uchun pop() dan foydalanamiz!
# agar pop() qimat kiritmasak bu uzi avtomatik listni ichidagi oxirgi qiymatni yulub oladi!
bozorlik = ['un', 'yog', 'sabzi', 'gurunch']
maxsulot = bozorlik.pop(1)
print(bozorlik)
print(maxsulot)
print("Men " + maxsulot + " sotib oldim" )
print("olinmagan maxsulotlar: ", bozorlik)

# uyga fazifa!

# 1
# 3 ta dostingizni ruyxatini yozing va ularga qisqa xabar yuboring

dostlar = ['Bahodir', 'Behzod', 'Abduroziq']
print('Dostlarni choyxonaga aytgin', dostlar[0])
print(dostlar[2], 'bugun choyxonaga borasanmi?')

# 2
# turli sonlarni kiriting va ular ustuda turli arifmetik amallarni bajaring!

sonlar = [12, -5, 105, 31, 45]
sonlar[1] = 5
sonlar.append(5)
sonlar.insert(3, 110)
print(sonlar[2] + sonlar[0] )
print(sonlar[3] * sonlar[4])

# 3
# pop() va append() dan foydalanamiz!

dostlar.remove("Abduroziq")
dostlar.append('Maxmudjon')
print("bugun choyxonaga kelganlar: ", dostlar)
print("kelmadi: Abduroziq") 

