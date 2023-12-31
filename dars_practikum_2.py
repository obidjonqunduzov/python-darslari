# Soz topish oyini!

from uzwords import words
import random


def get_word():
	word = random.choice(words)
	while '-' in word or ' ' in word:
		word = random.choice(words)
	return word.upper()


def display(user_letters,word):
	display_letter = ""
	for letter in word:
		if letter in user_letters.upper():
			display_letter +=letter
		else:
			display_letter += '-'
	return display_letter

def play():
	word = get_word()
	word_letters = set(word) # sozdagi harflar
	user_letters = ''
	print(f"  Men {len(word)} xonali soz uyladim. Topa olasizmi?")

	while len(word_letters)>0:
		print(display(user_letters,word))
		if len(user_letters)>0:
			print(f"Shu vaqtgacha kiritgan harflaringiz! {user_letters}")

		letter = input("Harf kiriting: ").upper()
		if letter in user_letters:
			print("Bu harfni oldin kritgansiz.Boshqa harf kiriting: ")
			continue
		elif letter in word:
			word_letters.remove(letter)
			print((f"{letter} harfi tuqri"))
		else:
			print("Bunday harf yuq")
		user_letters += letter
	print(f"Tabriklayman! {word} suzini {len(user_letters)} ta urunishda topdingiz!.")

