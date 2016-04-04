from __future__ import division

# does repeats, needs fix
def bestLine(points):
	lines = {}
	for s in points:
		for t in points - {s}:
			l = getLine(s, t)
			if l not in lines:
				lines[l] = 1
			else:
				lines[l] += 1
	print lines
			
def getSlope(s, t):
	return (s[1] - t[1]) / (s[0] - t[0])

def getYIntercept(s, m):
	return (m * (0-s[0])) + s[1]

def getLine(s, t):
	m = getSlope(s, t)
	b = getYIntercept(s, m)
	return (m, b)

a = (-1,-1)
b = (0,0)
c = (1,1)

l = {a,b,c}

bestLine(l)