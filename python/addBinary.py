def addBinary(a, b):
	a10 = int(a, 2)
	b10 = int(b, 2)
	ans = bin(a10 + b10)
	ans = ans[2:]
	return ans

print addBinary('111', '10')