import math

def reverse(string):
	s = list(string)
	mid = len(s) / 2
	for i in range(0, mid):
		s[i], s[-(i + 1)] = s[-(i + 1)], s[i]
	return ''.join(s)

print reverse("abcdef")
print reverse("abcde")


