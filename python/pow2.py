def isPow2(n):
	p = n.bit_length()
	m = 1
	m = m << p - 1
	if m == n:
		return True
	else:
		return False

def isPow2_(n):
	if n == 0:
		return False
	if (n & (n - 1)) == 0:
		return True
	else:
		return False

print isPow2(1024)
print isPow2_(1024)
