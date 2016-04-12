import sys
import itertools

def findGold(inp):
	k = int(inp[0])
	c = int(inp[1])
	s = int(inp[2])
	origins = list(itertools.product('LG', repeat = k))
	fractals = [buildFractal(''.join(f), c) for f in origins]
	result = choosePos(fractals, s, -1, [])
	if result is None:
		return 'IMPOSSIBLE'
	else:
		result = [str(i + 1) for i in result]
		return ' '.join(result)

def choosePos(fractals, s, last, ans):
	if s == 0:
		return None
	l = len(fractals[0])
	positions = {}
	for i in range(last + 1, l):
		if i in ans:
			continue
		newFractals = [f for f in fractals if f[i] != 'G']
		positions[i] = newFractals
		if len(newFractals) < 2:
			ans.append(i)
			return ans
	i = getSmallestKey(positions)
	ans.append(i)
	result = choosePos(positions[i], s - 1, i, ans)
	if result is not None:
		return result
	return None

def getSmallestKey(d):
	smallestK = -1
	smallest = -1
	for k in d.keys():
		if smallest == -1:
			smallestK = k
			smallest = len(d[k])
		elif len(d[k]) < smallest:
			smallestK = k
			smallest = len(d[k])
	return smallestK

def buildFractal(frac, c):
	k = len(frac)
	ans = frac
	for i in range(1, c):
		newAns = ""
		for char in ans:
			if char == 'L':
				newAns += frac
			else:
				newAns += ''.join(['G' for _ in range(0, k)])
		ans = newAns
	return ans

print findGold((65,5,65))

# with open(sys.argv[2]) as inf:
# 	lines = inf.readlines()
# 	lines = [l.strip('\n') for l in lines]
# 	lines = [l.split(' ') for l in lines]

# outName = sys.argv[1] + "Output.txt"
# ouf = open(outName, 'w')
# for i in range(1, int(lines[0][0]) + 1):
# 	ouf.write("Case" + " #" + str(i) + ": " + findGold(tuple(lines[i])) + '\n')