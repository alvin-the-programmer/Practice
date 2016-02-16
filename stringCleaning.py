def answer(chunk, word):
	strings = []
	explored = []
	rmWord(chunk, word, strings, explored)
	strings.sort()
	return strings[0]

def rmWord(chunk, word, strings, explored):
	positions = [i for i in range(len(chunk)) if chunk.startswith(word, i)]
	if not positions:
		strings.append(chunk)
	for i in positions:
		newChunk = chunk[:i] +chunk[i + len(word):]
		if newChunk not in explored:
			explored.append(newChunk);
			rmWord(newChunk, word, strings, explored)


print answer("lololololo", "lol")
print answer("goodgooogoogfogoood", "goo")