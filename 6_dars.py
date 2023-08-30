
# list royxatini davomi...
# kichik harflar xar doim katta xarflardan keyin keladi!

cars = ['mers', 'volvo', 'ferarri', 'bmw', 'opel']

# bu ruyxatni alfabet buyicha ketme-ket joylashtirish uchun sort() dan foydalanamiz!

cars.sort()
print(cars)
# yoki
print(sorted(cars))

# Agar shu ruyxatni chappasiga yozmoqchi bolsak sort(reverse=True) dan foydalanamiz!

cars.sort(reverse = True)
print(cars)
# Yoki
print(sorted(cars, reverse=True))

# shu ruyxatni aylantirsak 180gradusga reverse() dan foydalanamiz!

cars.reverse()
print(cars)

# uzunliginin len() orqali xisoblaymiz!

print(len(cars))

# range() oraliqdagi sonlarni chiqaradi!

sonlar = list(range(0,11))
print(sonlar)

# toq sonlar olish uchun
toq_sonlar = list(range(0, 20,2))
print(toq_sonlar)

# urtacha qiymat uchun max() foydalanamiz
max_sonlar = max(toq_sonlar)
print(max_sonlar)

# eng kam qiymat uchun min() dan foydalanamiz!

min_sonlar = min(toq_sonlar)
print(min_sonlar)

narxlar = [35, 4567, 54, 21, 3, 837]

#qiymatlar yigindisini topish uchun sum() dan foydalanamiz!

print(sum(narxlar))

# shu ruyxatdan nusxa kuchirish uchun (:) dan foydalanamiz!

my_cars = cars[:]
print(my_cars)

# Turple uzgarmas ruyxat

games = ('car', 'toys', 'snake', 'lizard')

# games[1] = 'teddy' bu amaliyot xato yane shunaqa () bolsa ichidagi qiymatlarni uzgartirib bolmaydi!!!
# games[1] = 'too' # xato!!!
print(games)

# agar juda uzgartirish zarur bolsa unda bunday qilamiz!

games = list(games) # yani endi xoxlagancha uzgartiramiz!
print(type(games))

# uyga vazifa
# 1
davlatlar = ['Uzbekistan', 'Tajikistan', 'USA', 'Russia', 'Turkiya']
print(davlatlar)

# 2
print(len(davlatlar))

# 3
print(sorted(davlatlar))

# 4
davlatlar.sort(reverse=True)
print(davlatlar)

# 5
print(davlatlar.sort(reverse=False))

# 6
davlatlar.reverse()
print(davlatlar)

# 7
qiymatlar = list(range(120,1200,2))
print(qiymatlar)

# 8
print(sum(qiymatlar))

# 9
max_qiymatlar = max(qiymatlar)
min_qiymatlar = min(qiymatlar)
print(max_qiymatlar - min_qiymatlar)

# 10
print(len(qiymatlar))

# 11
print(qiymatlar[0:21])
print(qiymatlar[240:261])
print(qiymatlar[520:])

# 12
taomlar = ['osh', 'norin', 'qrutob', 'beshbarmoq', 'mantu']
print(taomlar)

nonushta = taomlar[:]
print(nonushta)

# 13
print(nonushta[0:3])
nonushta.append(['asal','xalvo'])
print(nonushta)

# 14
nonushta = tuple(nonushta)
print(type(nonushta))

nonushta =list(nonushta)
print(type(nonushta))

nonushta[0] = ['qaymoq', 'non']
print(nonushta)