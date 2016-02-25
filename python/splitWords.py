def splitWords(s, d):
	if s in d:
		return s
	for i in range(len(s)):
		prefix = s[:i]
		suffix = s[i:]
		if prefix in d:
			remainder = splitWords(suffix, d)
			if remainder is not None:
				return prefix + ' ' + remainder
	return None

s = 'peanutbutter'
d = {'pea', 'nut', 'but' ,'butt', 'butter', 'utter'}
print splitWords(s, d)