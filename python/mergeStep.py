def merge(a, b):
	ans = []
	while a or b:
		if a and not b:
			ans.append(a.pop(0))
		elif b and not a:
			ans.append(b.pop(0))
		elif a < b:
			ans.append(a.pop(0))
		else:
			ans.append(b.pop(0))
	return ans

a = [5, 10, 15, 20, 25, 50, 75, 100, 101]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 18, 27, 81, 90, 99, 101, 103, 300]
print merge(a, b)