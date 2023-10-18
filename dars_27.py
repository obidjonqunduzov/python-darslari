# Fayllar bilan ishlashni o'rganamiz!

with open("pi.txt") as fayl:
    pi = fayl.read()

pi = pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
pi = pi.replace('\n','') # qator tashlash belgisini almashtiramiz
pi = float(pi) # matnni float (o'nlik) songa o'tkazamiz
print(pi)