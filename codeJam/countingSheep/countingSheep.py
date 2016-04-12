import sys

def countSheep(n):
	if n == 0:
		return 'INSOMNIA'
	seen = set()
	i = 1
	while len(seen) < 10:
		num = str(i * n)
		seen.update([char for char in num])
		i += 1
		if len(seen) == 10:
			return int(num)

with open(sys.argv[2]) as inf:
	lines = inf.readlines()
	lines = [l.strip('\n') for l in lines]

outName = sys.argv[1] + "Output.txt"
ouf = open(outName, 'w')
for i in range(1, int(lines[0]) + 1):
	ouf.write("Case" + " #" + str(i) + ": " + str(countSheep(int(lines[i]))) + "\n")