# operations using onling the addition (+) operator

def negate(a):
	if a < 0:
		increment = 1
	elif a > 0:
		increment = -1
	else:
		return 0
	s = 0
	for i in range(0, abs(a)):
		s += increment
	return s

def subtract(a, b):
	return a + negate(b)

def multiply(a, b):
	s = 0
	for i in range(0, abs(b)):
		s += abs(a)
	if (a < 0) ^ (b < 0):
		s = negate(s)
	return s

def divide(a, b):
	s = abs(a)
	i = 0
	while s > 0:
		s = subtract(s, abs(b))
		i += 1
	if (a < 0) ^ (b < 0):
		i = negate(i)
	return i