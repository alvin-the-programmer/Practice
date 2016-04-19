# O(nlogn) time, O(n) space

def arrayLess(n):
	s = sorted(n)
	s = s[::-1]
	last = None
	ans = {}
	for i in range(0, len(s)):
		if s[i] != last:
			ans[s[i]] = len(s[:i])
			last = s[i]
	return [ans[c] for c in n]

print arrayLess([9,2,5,1,6,7,3,2])
