import time
import math

def pythagoreanTriplet(n):
	for a in range(1, n):
		for b in range(a, n):
			c = math.sqrt(a**2 + b**2)
			if a + b + c == n:
				return a * b * c
	return -1

start = time.clock()
print pythagoreanTriplet(1000)
end = time.clock()
print end - start