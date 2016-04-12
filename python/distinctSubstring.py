def getDistinct(s):
	longest = s[0]
	i = 0
	latestPos = {s[0]: 0}
	for j in range(1, len(s)):
		if s[j] in latestPos:
			if latestPos[s[j]] >= i:
				i = latestPos[s[j]] + 1
		latestPos[s[j]] = j
		if len(s[i:j + 1]) > len(longest):
			longest = s[i:j + 1]
	return longest

# O(n) time compexity

print getDistinct('aaaaaaaaaa')
print getDistinct('aaabbaaaaa')
print getDistinct('banana')
print getDistinct('alvin')
print getDistinct('geeksforgeeks')