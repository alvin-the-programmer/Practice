def permutation(a, b):
	asort = sorted(a)
	bsort = sorted(b)
	if asort == bsort:
		return True
	else:
		return False

def permutation2(a, b):
	charList = list(a)
	for char in b:
		if char in charList:
			charList.remove(char)
		else:
			return False
	if charList:
		return False
	else:
		return True

def permutation3(a, b):
	charDict = dict()
	if len(a) != len(b):
		return False
	for char in a:
		if char in charDict:
			charDict[char] += 1
		else:
			charDict[char] = 1
	for char in b:
		if char in charDict:
			if charDict[char] == 0:
				return False;
			charDict[char] -= 1
		else:
			return False
	return True

