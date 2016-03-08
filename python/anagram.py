from collections import Counter
from copy import deepcopy

def containsAnagram(a, b):
	lista = list(a)
	for i in range(0, len(b) - len(a) + 1):
		chars = lista[:]
		for j in range(i, i + len(a)):
			if b[j] in chars:
				chars.remove(b[j])
				if not chars:
					return True
			else:
				break
	return False

def containsAnagram2(a, b):
	counta = Counter(a)
	substrings = [b[i:i+len(a)] for i in range(0, len(b) - len(a) + 1)]
	return any(Counter(subStr) == counta for subStr in substrings)

print containsAnagram('npe','pencilcase')
print containsAnagram2('npe','pencilcase')
print containsAnagram('case','pencilcase')
print containsAnagram2('case','pencilcase')
print containsAnagram('esca','pencilcase')
print containsAnagram2('esca','pencilcase')
print containsAnagram('abcdef','abczdefabc')
print containsAnagram2('abcdef','abczdefabc')
print containsAnagram('abcdef','abczdefhij')
print containsAnagram2('abcdef','abczdefhij')



