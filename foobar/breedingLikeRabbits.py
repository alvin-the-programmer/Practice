def zombit(n, cache):
	if n not in cache:
		h = n / 2
		if h * 2 == n:
			cache[n] = zombit(h, cache) + zombit(h + 1, cache) + h
		else:
			cache[n] = zombit(h - 1, cache) + zombit(h, cache) + 1
	return cache[n]

def searchEven(low, high, target, cache):
	if low >= high:
		return "None"
	mid = (low + high) / 2
	if mid % 2 == 1:
		mid += 1
	result = zombit(mid, cache)
	if result == target:
		return str(mid)
	elif result < target:
		return searchEven(mid + 1, high, target, cache)
	else:
		return searchEven(low, mid - 1, target, cache)

def searchOdd(low, high, target, cache):
	if low >= high:
		return "None"
	mid = (low + high) / 2
	if mid % 2 == 0:
		mid += 1
	result = zombit(mid, cache)
	if result == target:
		return str(mid)
	elif result < target:
		return searchOdd(mid + 1, high, target, cache)
	else:
		return searchOdd(low, mid - 1, target, cache)

def answer(str_S):
	s = int(str_S)
	cache = {0: 1, 1: 1, 2: 2}
	oddAns = searchOdd(0, s, s, cache)
	if oddAns != "None":
		return oddAns
	else:
		return searchEven(0, s, s, cache)