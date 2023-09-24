
from transliterate import to_cyrillic, to_latin


# isascii() jadval

matn = input(" 'lotin' yoki 'криллда' Soz kiriting: ")

if matn.isascii():
	print(to_cyrillic(matn))
else:
	print(to_latin(matn))