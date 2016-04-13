# matrix such that an element is >= the element to the right and the element below
def sortMatrix(m):
	if len(m) < len(m[0]):
		return mergeLists(m)
	else:
		newMatrix = []
		for i in range(0, len(m[0])):
			newL = []
			for l in m:
				newL.append(l[i])		
			newMatrix.append(newL)
		return mergeLists(newMatrix)

def mergeLists(lists):
	result = []
	for l in lists:
		result = merge(l, result)
	return result

def merge(alist, blist):
	ans = []
	a = alist[:]
	b = blist[:]
	while a or b:
		if a and not b:
			ans.append(a.pop(0))
		elif b and not a:
			ans.append(b.pop(0))
		elif a > b:
			ans.append(a.pop(0))
		else:
			ans.append(b.pop(0))
	return ans


m = [
	[100, 90, 80, 70],
	[92, 90, 77, 59],
	[69, 68, 71, 56],
	[64, 30, 29, 29],
	[27, 24, 22, 21],
]

print sortMatrix(m)