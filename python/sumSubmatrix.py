import numpy

def sumSubmatrix(m, left, right, bottom, top):
	subSum = 0
	for i in range(top, bottom + 1):
		for j in range(left, right + 1):
			subSum += m[i][j]
	return subSum

m = numpy.random.random_integers(1, 9, (9, 9))
print m
print sumSubmatrix(m, 6, 8, 1, 0)

