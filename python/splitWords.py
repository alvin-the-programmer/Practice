def splitWords(s, d, m):
	if s in d:
		return s
	elif s in m.keys():
		return m[s]
	else:
		for i in range(len(s)):
			prefix = s[:i]
			suffix = s[i:]
			if prefix in d:
				remainder = splitWords(suffix, d, m)
				if remainder is not None:
					split = prefix + ' ' + remainder
					m[s] = split
					return split
		m[s] = None
		return None

s = 'peanutbutter'
d = {'pea', 'nut', 'but' ,'butt', 'butter', 'utter'}
memo = {}
print splitWords(s, d, memo)

s = 'aaaaaaaaaab'
d = {'a','aa','aaa','aaaa', 'aaaaa', 'aaaaaa', 'aaaaaaa', 'aaaaaaaa', 'aaaaaaaaa'}
memo = {}
print splitWords(s, d, memo)