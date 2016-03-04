import math

def isPrime(n):
	if n == 2:
		return True
	if n % 2 == 0:
		return False
	for i in range(2, int(math.sqrt(n)) + 1):
   		if n % i == 0:
   			return False
  	return True

def sumPrimes(n):
	s = 0
	for i in range(2, n):
		if isPrime(i):
			s += i
	return s

print sumPrimes(2000000)