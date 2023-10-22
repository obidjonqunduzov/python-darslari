# Fayllar bilan ishlash


with open('C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\pi.txt') as fayl:
    pi = fayl.read()
    pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
    pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz

print(pi)

with open ('C:\\Users\\HP\\Documents\\GitHub\\python-darslari\\talabalar.txt') as fayl_2:
    talabalar = fayl_2.readlines()
    talabalar = [talaba.rstrip() for talaba in talabalar]

print(talabalar)
