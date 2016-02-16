def reverseVowels(string):
	vowels = {'a', 'e', 'i', 'o', 'u'}
	stack = []
	for c in string:
		if c in vowels:
			stack.append(c)
	reverse = list(string)
	for i in range(0, len(reverse)):
		if reverse[i] in vowels:
			reverse[i] = stack.pop()
	return ''.join(reverse)

print reverseVowels("abcdefghi")
