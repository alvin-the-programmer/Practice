def sortAnagrams(words):
	sortChars = {}
	for w in words:
		wsorted = ''.join(sorted(w))
		if wsorted in sortChars:
			sortChars[wsorted].append(w)
		else:
			sortChars[wsorted] = [w]
	ans = []
	for l in sortChars.values():
		ans.extend(l)
	return ans

w = ['alvin', 'tac', 'cat', 'nivla', 'cat', 'vinal', 'dog', 'god', 'supocto','taco', 'octopus', 'computer']
print sortAnagrams(w)