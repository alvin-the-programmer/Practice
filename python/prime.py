import math

def isPrime(n):
	if n == 2 or n == 3:
		return True
	if n % 2 == 0:
		return False
	h = int(math.ceil(math.sqrt(n))) 
	for i in range(2, h):
		if n % i == 0:
			return False
	return True

def prime(n):
	pCount = 0
	i = 2
	while True:
		if isPrime(i):
			pCount += 1
		if pCount == n:
			return i
		i += 1

print prime(10001)