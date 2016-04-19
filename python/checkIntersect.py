# [a,b) and [c,d)
def checkIntersect(a, b, c, d):
	if (c >= a and c < b) or (d - 1 >= a and d - 1 < b) or (a >= c and a < d) or (b - 1 >= c and b - 1 < d):
		return True
	else:
		return False

print checkIntersect(5,7,10,12)