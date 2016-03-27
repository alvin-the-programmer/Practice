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
	currMoves = [0 for _ in range(0, n)]
	currMoves[n - 1] = 1
	lastMoves = [0 for _ in range(0, n)]
	for i in range(0, t):
		currMoves, lastMoves = lastMoves, currMoves
		for j in range(0, n):
			currMoves[j] = lastMoves[j]
			if j == n - 1:
				continue
			if j > 0:
				currMoves[j] += lastMoves[j - 1]
			currMoves[j] += lastMoves[j + 1]
			currMoves[j] %= 123454321
	return currMoves[0]

print bruteAnswer(15,12)
print answer(15,12)
