def stripSpace(s):
	words = s.split()
	return ' '.join(words)


def stripSpace2(s):
	words = []
	word = []
	for i in range(len(s)):
		if s[i] is not ' ':
			word.append(s[i])
		elif word:
			words.append(''.join(word))
			word = []
	if word:
		words.append(''.join(word))
	return ' '.join(words)

print stripSpace2('hi      i    am   alvin ')
