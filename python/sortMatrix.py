from heapq import heappush, heappop
from time import time

# matrix such that an element is >= the element to the right
# and the element below

# O(nk*lognk) runtime
def sortMatrixSlow(m):
	if len(m) < len(m[0]):
		return mergeLists()
	else:
		newMatrix = []
		for i in range(0, len(m[0])):
			newL = []
			for l in m:
				newL.append(l[i])		
			newMatrix.append(newL)
		return mergeLists(newMatrix)

def mergeLists(lists):
	lists = lists[:]
	result = []
	for l in lists:
		result = merge(l, result)
	return result[::-1]

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

# for k by n matrix O(kn*log(k)) runtime if k < n
def sortMatrixFast(m):
	if len(m) < len(m[0]):
		return mergeListsQ()
	else:
		newMatrix = []
		for i in range(0, len(m[0])):
			newL = []
			for l in m:
				newL.append(l[i])		
			newMatrix.append(newL)
		return mergeListsQ(newMatrix)

def mergeListsQ(lists):
	lists = lists[:]
	h = []
	for i in range(0, len(lists)):
		pair = (lists[i].pop(), i)
		heappush(h, pair)
	ans = []
	while h:
		value, i = heappop(h)
		ans.append(value)
		if lists[i]:
			pair = (lists[i].pop(), i)
			heappush(h, pair)
	return ans


m = [
	[100, 90, 80, 70, 68, 50],
	[92, 90, 77, 59, 55, 33],
	[69, 68, 71, 56, 54, 33],
	[64, 30, 29, 29, 22, 16],
	[27, 24, 22, 21, 13, 11],
	[23, 21, 18, 16, 11, 10]
]

print sortMatrixFast(m)
