# ALVIN ZABLAN
# Professor Saad
# CSCI 395
# Homework 1
# Problem 1 part d 
# run with 'python coinChange.py'

def value(a, c):
	s = 0
	for i in range(1, a[0] + 1):
		s += a[i] * c[i]
	return s

def count(a):
	s = 0
	for i in range(1, a[0] + 1):
		s += a[i]
	return s

def skip(a,c,d,M):
	if a[0] == d:
		a = [0, '-', '-', '-']
	else:
		a[0] += 1
		a[a[0]] = 0

def next(a, c, d, m):
	if a[0] < d:
		a[0] += 1
		a[a[0]] = 0
	else:
		if a[a[0]] < m / c[a[0]]:
			a[a[0]] += 1
		else:
			while a[a[0]] == m / c[a[0]]:
				a[a[0]] = '-'
				a[0] -= 1
				if a[0] == 0:
					return
			a[a[0]] += 1

def search(a, c, d, m):
	best = m
	checked = 0
	while a[0] > 0:
		checked += 1
		if value(a, c) or count(a) > best:
			skip(a,c,d,m)
		if a[0] == d:
			if value(a,c) == m and count(a) < best:
				best = count(a)
				besta = a[:]
		next(a, c, d, m)
	print "num checked:", checked
	return besta

def slowSearch(a, c, d, m):
	best = m
	checked = 0
	while a[0] > 0:
		checked += 1
		if a[0] == d:
			if value(a,c) == m and count(a) < best:
				best = count(a)
				besta = a[:]
		next(a, c, d, m)
	print "num checked:", checked
	return besta

coins = [None, 25, 15, 1]
numCoins = 3

arr = [1, 0, 0 ,0]
print search(arr, coins, numCoins, 687)

arr = [1, 0, 0 ,0]
print slowSearch(arr, coins, numCoins, 687)

