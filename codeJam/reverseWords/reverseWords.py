import sys

def reverseWords(s):
	words = s.split(' ')
	words = words[::-1]
	return ' '.join(words)

with open(sys.argv[2]) as inf:
	lines = inf.readlines()
	lines = [l.strip('\n') for l in lines]

outName = sys.argv[1] + "Output.txt"
ouf = open(outName, 'w')
for i in range(1, int(lines[0]) + 1):
	ouf.write("Case" + " #" + str(i) + ": " + reverseWords(lines[i]) + "\n")