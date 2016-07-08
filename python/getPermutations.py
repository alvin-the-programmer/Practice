def getPerms(stri):
	chars = list(stri)
	perms = []
	getPerms_(chars, perms, "")
	return perms

def getPerms_(chars, perms, s):
	if len(chars) == 0:
		perms.append(s)
	else:
		charSet = set(chars)
		for c in charSet:
			newChars = chars[:]
			newChars.remove(c)
			newS = s + c
			getPerms_(newChars, perms, newS)

print getPerms("aaa")
print getPerms("abc")
print getPerms("abca")
print getPerms("bottle")
