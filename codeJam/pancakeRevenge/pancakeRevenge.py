import sys

def countFlips(s):
	up = ''.join(['+' for i in range(0, len(s))])
	down = ''.join(['-' for i in range(0, len(s))])
	count = 0
	while not (s == up or s == down):
		if s == up:
			return count
		if s == down:
			return count + 1
		s = flip(s)
		count += 1
	if s == up:
		return count
	else:
		return count + 1

def flip(s):
	for i in range(0, len(s) - 1):
		if s[i] != s[i + 1]:
			if s[0] == '-':
				return ''.join(['+' for _ in range(0, i + 1)]) + s[i + 1:]
			else:
				return ''.join(['-' for _ in range(0, i + 1)]) + s[i + 1:]

with open(sys.argv[2]) as inf:
	lines = inf.readlines()
	lines = [l.strip('\n') for l in lines]

outName = sys.argv[1] + "Output.txt"
ouf = open(outName, 'w')
for i in range(1, int(lines[0]) + 1):
	ouf.write("Case" + " #" + str(i) + ": " + str(countFlips(lines[i])) + "\n")