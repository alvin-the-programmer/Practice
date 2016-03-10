def pow5(n):
	for i in range(1, n):
		if 5**i == n:
			return True
		elif 5**i > n:
			return False
