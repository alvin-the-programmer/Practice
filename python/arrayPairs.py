import random
from time import time

def arrayPairs(a, x):
	pairs = set()
	numMap = {}
	for i in range(0, len(a)):
		if a[i] in numMap:
			numMap[a[i]].append(i)
		else:
			numMap[a[i]] = [i]
	for i in range(0, len(a)):
		c = x - a[i]
		if c in numMap:
			for j in numMap[c]:
				if i != j:
					if (i, j) not in pairs and (j, i) not in pairs:
						pairs.add((i, j))
	return pairs

def arrayPairsBrute(a, x):
	pairs = set()
	for i in range(0, len(a)):
		for j in range(0, len(a)):
			if a[i] + a[j] == x and i != j:
				if (i, j) not in pairs and (j, i) not in pairs:
					pairs.add((i, j))
	return pairs

a = [random.randrange(-10, 10) for i in range(0, 10001)]
print 'finished initializing array...'

start1 = time()
arrayPairs(a, 3)
end1 = time()
print 'fast: ', end1 - start1

start2 = time()
arrayPairsBrute(a, 3)
end2 = time()
print 'slow: ', end2 - start2

