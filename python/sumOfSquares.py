def getSum(n):
	best = [[1 for i in range(0, n)]]
	squares = getSquares(n)
	findSum(n, [], squares, best)
	print sum(best[0])
	return best[0]

def findSum(n, ans, squares, best):
	if n < 0:
		return
	if len(ans) >= len(best[0]):
		return
	if n == 0 and len(ans) < len(best[0]):
		best[0] = ans
		return
	for s in squares:
		newAns = ans[:]
		newAns.append(s)
		findSum(n - s, newAns, squares, best)

def getSquares(n):
	ans = []
	i = 1
	while i**2 <= n:
		ans.append(i**2)
		i += 1
	return ans[::-1]

# brute force, O(n^2) time complexity
print getSum(12345)