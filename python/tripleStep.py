
def tripleStep(n, results, x=0, y=0, z=0):
	remainder = n - (x + 2*y + 3*z)
	if remainder == 0:
		results.append((x,y,z))
		return
	if remainder >= 3:
		tripleStep(n,results,x,y,z+1)
	if remainder >= 2:
		tripleStep(n,results,x,y+1,z)
	tripleStep(n,results,x+1,y,z)

def countTripleStep(n):
	results = []
	tripleStep(n,results)
	print len(results)


def countWays(n):
	if n < 0:
		return 0
	elif n == 0:
		return 1
	else:
		return countWays(n-1) + countWays(n-2) + countWays(n-3)

countTripleStep(6)
print countWays(6)