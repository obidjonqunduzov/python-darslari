# Fayllar bilan ishlashni o'rganamiz!

file = open("pi.txt.py")
PI = file.read()
print(PI)
file.close()

with open('pi.txt') as fayl:
    pi = fayl.read()