import numpy

# O(nm) time, O(1) space
def zeroMatrix(m):
	print m
	zeroFirstRow, zeroFirstCol = findZeros(m)
	for r in range(1, len(m)):
		if m[r][0] == -1:
			zeroRow(r, m)
	for c in range(1, len(m[0])):
		if m[0][c] == -1:
			zeroCol(c, m)
	if zeroFirstRow:
		zeroRow(0, m)
	if zeroFirstCol:
		zeroCol(0, m)
	print m

def findZeros(m):
	zeroRow = False
	zeroCol = False
	for r in range(0, len(m)):
		if m[r][0] == 0:
			zeroCol = True
			break
	for c in range(0, len(m[0])):
		if m[0][c] == 0:
			zeroRow = True
			break
	for row in range(0, len(m)):
		for col in range(0, len(m[0])):
			if m[row][col] == 0:
				m[0][col] = -1
				m[row][0] = -1
	return zeroRow, zeroCol

def zeroRow(row, m):
	for i in range(0, len(m[0])):
		m[row][i] = 0

def zeroCol(col, m):
	for i in range(0, len(m)):
		m[i][col] = 0;

m = numpy.random.random_integers(1,9, (9,9))
m[0][1] = 0
m[3][7] = 0
m[3][0] = 0
m[8][8] = 0
m[5][1] = 0
zeroMatrix(m)