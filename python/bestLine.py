from __future__ import division

# O(n^2) time, calculates line for every pair of points
# beware of floating point comparison, representing slope as rational fraction would be best.
def bestLine(points):
	# lines represented by pair (slope, y-intercept)
	# or (None, x-intercept) if slope undefined in case of vertical line
	lines = {}
	pairs = getPairs(points)
	for pair in pairs:
		l = getLine(pair[0], pair[1])
		if l in lines:
			if pair[0] not in lines[l]:
				lines[l].add(pair[0])
			if pair[1] not in lines[l]:
				lines[l].add(pair[1])
		else:
			lines[l] = {pair[0], pair[1]}
	return max([len(val) for val in lines.values()])
			
def getSlope(s, t):
	if s[0] - t[0] == 0:
		return None
	else:
		return (s[1] - t[1]) / (s[0] - t[0])

def getYIntercept(s, m):
	if m is None:
		return s[0]
	else:
		return (m * (-s[0])) + s[1]

def getLine(s, t):
	m = getSlope(s, t)
	b = getYIntercept(s, m)
	return (m, b)

def getPairs(inputSet):
	pairs = []
	done = set()
	for s in inputSet:
		for t in inputSet - {s}:
			if (s, t) not in done:
				pairs.append((s, t))
				done.add((s, t))
				done.add((t, s))
	return pairs

p = {(-1,-1), (0,0), (1,1), (4, 4) ,(1,4), (1,6), (1, 20), (1,-20)}
print bestLine(p)