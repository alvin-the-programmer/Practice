from random import randrange

# O(n) time, O(n) space
def shuffle(a):
	values = a[:]
	ans = []
	while len(ans) != len(values):
		k = randrange(0, len(values) - len(ans))
		ans.append(mark(values, k))
	return ans

def mark(a, k):
	count = -1
	for i in range(0, len(a)):
		if a[i] is None:
			continue
		else:
			count += 1
			if count == k:
				ans = a[i]
				a[i] = None
				return ans

a = [0,1,2,3,4,5,6,7,8,9]
print shuffle(a)
