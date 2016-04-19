def lexicoSubstr(s):
	for i in range(1, len(s)):
		if s[i] > s[0]:
			return s[i:]

a = 'catinthehat'
b = "huntercollege"
c = "xwvza"
d = "ddanger"
print lexicoSubstr(a)
print lexicoSubstr(b)
print lexicoSubstr(c)
print lexicoSubstr(d)