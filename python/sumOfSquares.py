from time import time

def getSquares(n):
	ans = []
	i = 1
	while i**2 <= n:
		ans.append(i**2)
		i += 1
	return ans[::-1]

def getShortestSqSumBrute(n):
	best = [[1 for i in range(0, n)]]
	squares = getSquares(n)
	findSumBrute(n, [], squares, best)
	return best[0]

def findSumBrute(n, ans, squares, best):
	if n < 0:
		return
	# if len(ans) >= len(best[0]):
	# 	return
	if n == 0 and len(ans) < len(best[0]):
		best[0] = ans
		return
	for s in squares:
		newAns = ans[:]
		newAns.append(s)
		findSumBrute(n - s, newAns, squares, best)
# brute force, O(n^2), O(1) space

def getShortestSqSum(n):
	sumsDict = {0: [], 1: [1]}
	squares = getSquares(n)
	return findSum(n, sumsDict, squares)

def findSum(n, sums, squares):
	if n in sums:
		return sums[n]
	best = [1 for i in range(0, n)]
	for s in squares:
		if s > n:
			continue
		ans = [s]
		ans.extend(findSum(n - s, sums, squares))
		if len(ans) < len(best):
			best = ans
	sums[n] = best
	return best
# dynamic programming, O(n) time, O(n) space

for i in range(0, 50):
	print i, "==============================================="
	start = time()
	getShortestSqSum(i)
	end = time()
	print 'dynamic programming: ', end - start
	start = time()
	getShortestSqSumBrute(i)
	end = time()
	print 'brute force: ', end - start
