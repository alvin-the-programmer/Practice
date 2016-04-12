import math
import sys

def jamCoin(inp):
	n = int(inp[0])
	j = int(inp[1])
	coins = getCoins(n)
	validCoins = {}
	for coin in coins:
		divisors = []
		for base in range(2, 11):
			num = int(coin, base)
			div = getDivisor(num)
			if div is not None:
				divisors.append(str(div))
			else:
				break
		if len(divisors) == 9:
			validCoins[str(coin)] = divisors
		if len(validCoins) == j:
			return validCoins

def formatSol(validCoins):
	ans = ""
	for c in validCoins.keys():
		ans += c + ' '
		ans += ' '.join(validCoins[c]) + '\n'
	return ans


def getCoins(n):
	bits = '0' + str(n - 2) + 'b'
	return ['1' + format(i, bits) + '1' for i in range(0, 2**(n - 2))]

def getDivisor(n):
	if n == 2 or n == 3:
		return None
	if n % 2 == 0:
		return 2
	h = int(math.ceil(math.sqrt(n))) 
	for i in range(2, h):
		if n % i == 0:
			return i
	return None

with open(sys.argv[2]) as inf:
	lines = inf.readlines()
	lines = [l.strip('\n') for l in lines]
	lines = [l.split(' ') for l in lines]

outName = sys.argv[1] + "Output.txt"
ouf = open(outName, 'w')
for i in range(1, int(lines[0][0]) + 1):
	ouf.write("Case" + " #" + str(i) + ":\n" + formatSol(jamCoin(tuple(lines[i]))))