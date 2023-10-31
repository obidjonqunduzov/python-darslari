# Fayllar bilan ishlash


with open('C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\fayllar_bilan_ishlash\\pi.txt') as fayl:
    pi = fayl.read()
    pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
    pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz

print(pi)

with open ('C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\fayllar_bilan_ishlash\\talabalar.txt') as fayl_2:
    talabalar = fayl_2.readlines()
    talabalar = [talaba.rstrip() for talaba in talabalar]

print(talabalar)

name_fayl = 'C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\fayllar_bilan_ishlash\\write_talabalar.txt'
name = 'Olim Olimov Hakimov'
age = 21
with open(name_fayl, 'w') as fayl_3:
    fayl_3.write(name +'\n')
    fayl_3.write(str(age)+'\n')
    
with open(name_fayl,'a') as fayl_3:
    fayl_3.write("Hasan Dusmetov \n")
    fayl_3.write('1998')



import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

with open('info','wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)

with open('info','rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

print(talaba1)