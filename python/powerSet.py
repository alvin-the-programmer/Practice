def powerSet(l):
	ans = []
	pSet(l, [], 0, ans)
	return ans

def pSet(l, a, n, ans):
	if n == len(l):
		ans.append(a)
	else:
		y = a[:]
		y.append(l[n])
		pSet(l, y, n + 1, ans)
		pSet(l, a[:], n + 1, ans)

print powerSet([1,2,3,4,5])