from collections import OrderedDict

def allBase(s):
	symbols = list(OrderedDict.fromkeys(s))
	base = len(symbols)
	values = [i for i in range(0, base)]
	values[0], values[1] = values[1], values[0]
	d = dict(zip(symbols, values))
	ans = [str(d[c]) for c in s]
	ans = ''.join(ans)
	return int(ans, base)

print allBase('11001001')
print allBase('cats')
print allBase('zig')