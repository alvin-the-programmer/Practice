def reverseWords(s):
	words = s.split()
	words = words[::-1]
	return ' '.join(words)

print reverseWords('hi i am alvin zablan')