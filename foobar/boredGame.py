def move(t, n, pos, lastPos, count):
	if (n - pos) > t:
		return
	if lastPos == n and pos != n:
		return
	if pos < 1 or pos > n:
		return
	if t == 0 and pos == n:
		count[0] += 1
		return
	elif t == 0:
		return
	move(t - 1, n, pos - 1, pos, count)
	move(t - 1, n, pos + 1, pos, count)
	move(t - 1, n, pos, pos, count)

def count(t, n):
	count = [0]
	move(t, n, 1, 1, count)
	return count[0]

def bruteAnswer(t, n):
	count = [0]
	move(t, n, 1, 1, count)
	return count[0] % 123454321

def answer(t, n):
	cache = {}
	return countNum(t, n, 0, cache)

# the number of ways to get from position p to the goal (position n - 1) in t moves = 
# number of ways to get to p - 1 in t - 1 moves + 
# number of ways to get to p + 1 in t - 1 moves +
# number of ways to get to p in t - 1 moves
def countNum(t, n, p, cache):
	key = str(t) + '/' + str(p)
	if key in cache:
		return cache[key]
	if n - p == 1:
		return 1
	if t == 0:
		return 0
	count = 0
	if p > 0:
		count += countNum(t - 1, n, p - 1, cache)
	if n - p > 1:
		count += countNum(t - 1, n, p + 1, cache)
	count += countNum(t - 1, n, p, cache)
	cache[key] = count % 123454321
	return cache[key]


