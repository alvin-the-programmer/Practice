def fib(x):
	if x == 1 or x == 2:
		return 1
	else:
		return fib(x - 1) + fib(x - 2)

def fibCount(x):
	last2 = 0
	last1 = 1
	print 'fib 1 = 1'
	for i in range(2, x + 1):
		f = last1 + last2
		print 'fib ' + str(i) + ' =',
		print f
		last2 = last1
		last1 = f

print fib(3)
print fib(4)
print fib(5)
print fib(6)
print fib(7)
print fib(8)

fibCount(8)

