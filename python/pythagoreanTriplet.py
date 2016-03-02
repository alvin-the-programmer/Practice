def pythagoreanTriplet(n):
	for a in range(1, n):
		for b in range(1, n):
			for c in range(1, n):
				if a**2 + b**2 == c**2 and a + b + c == n:
					return a * b * c
	return -1

print pythagoreanTriplet(1000)