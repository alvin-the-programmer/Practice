import numpy

def zeroMatrix(m):
	print m
	rows, cols = findZeros(m)
	for r in rows:
		zeroRow(r, m)
	for c in cols:
		zeroCol(c, m)
	print m

def findZeros(m):
	zeroRows = set()
	zeroCols = set()
	for row in range(0, len(m)):
		for col in range(0, len(m[0])):
			if m[row][col] == 0:
				zeroRows.add(row)
				zeroCols.add(col)
	return zeroRows, zeroCols

def zeroRow(row, m):
	for i in range(0, len(m[0])):
		m[row][i] = 0

def zeroCol(col, m):
	for i in range(0, len(m)):
		m[i][col] = 0;

m = numpy.random.random_integers(1,9, (9,9))
m[0][1] = 0
m[3][7] = 0
m[8][8] = 0
m[5][1] = 0

zeroMatrix(m)