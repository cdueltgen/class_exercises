def count(filename):
	f = open(filename)
	text = f.read()
	text.lower()

	letters = [0] * 26
	for letter in text:
		index = ord(letter) - ord("a")
		if index >=0 and index < 26:
			letters[index] += 1

	return letters

for letter in string.letters:
	text.count(letter)
