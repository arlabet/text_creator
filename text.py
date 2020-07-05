def sentence_maker(phrase):
	capitalized = phrase.capitalize()
	if phrase.startswith(("how", "why", "what")):
		marq = capitalized + "? "
	else:
		marq = capitalized + ". "
	return (marq)

phrase = ""

all_text = []

while (phrase != "\end"):
	phrase = input("Say something: ")
	all_text.append(phrase)

new_text = []

for element in all_text:
	element = sentence_maker(element)
	new_text.append(element)

new_text.remove(new_text[-1])

print(*new_text)
