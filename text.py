def sentence_maker(phrase):
	capitalized = phrase.capitalize()
	if phrase.startswith(("how", "why", "what", "where")):
		marq = capitalized + "? "
	else:
		marq = capitalized + ". "
	return (marq)

phrase = ""

all_text = []

while (phrase != "\end"):
	phrase = input("Say something: ")
	phrase_bet = sentence_maker(phrase)
	all_text.append(phrase_bet)

all_text.remove(all_text[-1])

print(*all_text)
