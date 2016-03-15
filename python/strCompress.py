def strCompress(s):
	freq = {}
	for char in s:
		if char not in freq:
			freq[char] = 1
		else:
			freq[char] += 1
	ans = ''
	for k in freq.keys():
		ans += str(k)
		ans += str(freq[k])
	return ans

print strCompress('alvinzablanisacomputersciencemajorpythonisthebestlanguageever')