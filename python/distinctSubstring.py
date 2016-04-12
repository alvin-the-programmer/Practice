def getDistinct(s):
	longest = ''
	i = 0
	for j in range(1, len(s) + 1):
		if len(s[i:j]) > len(longest):
			longest = s[i:j]
		if j < len(s):
			repeat = s.find(s[j], i, j)
			if repeat > -1:
				i = repeat + 1
	return longest

# need to use dp insteach of find()

print getDistinct('banana')
print getDistinct('alvin')

