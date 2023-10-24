import pickle

# 1

with open('C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\fayllar_bilan_ishlash\\write_talabalar.txt') as file:
    pi = file.read()
pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
pi = pi.replace(' ','')

# Tug'ilgan kunim pi da bormi?
bdate = '1'
print(bdate in pi)


# 2

name_fayl = 'C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\fayllar_bilan_ishlash\\write_book.txt'

while True:
    name = input("O'qigan kitoblaringizni kiriting: (Agar boshqa kitob kritmasangiz 'tugadi' tugmasini bosing) : ")
    page = int(input("Kitobingizni sahifasini ham kiriting: "))
    if name == 'tugadi':
        break
    with open(name_fayl, 'a') as fayl:
        fayl.write(name +'\n')
        fayl.write(str(page)+'\n')


