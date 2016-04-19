def buyTwoSlow(cost, items):
	for i in range(0, len(items) - 1):
		for j in range(0, len(items)):
			if items[i] + items[j] == cost:
				return i, j

def buyTwoFast(cost, items):
	index = {items[i]:i for i in range(0, len(items))}
	for i in range(0, len(items)):
		if cost - items[i] in index:
			return i, index[cost - items[i]]

print buyTwoSlow(100, [32, 75,10, 25,28])
print buyTwoFast(100, [32, 75,10, 25,28])
