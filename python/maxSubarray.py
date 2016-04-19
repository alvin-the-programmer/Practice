def maxSubarraySum(l):
	maximum = 0
	thisMax = 0
	for v in l:
		thisMax = max(0, thisMax + v)
		maximum = max(maximum, thisMax)
	return maximum

l = [10, 25, 5, 5]
k = [10, -15, 5 , 6]

print maxSubarraySum(l)
print maxSubarraySum(k)
