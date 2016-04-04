def subSortSlow(a):
	asorted = sorted(a)
	for i in range(0, len(a)):
		if a[i] != asorted[i]:
			left = i
			break
	for j in range(len(a) - 1, -1, -1):
		if a[j] != asorted[j]:
			right = j
			break
	return (left, right)
# O(nlogn)

def subSort(a):
	for i in range(0, len(a) - 1):
		if a[i] > a[i + 1]:
			left = i
			break
	for j in range(len(a) - 1, 0, -1):
		if a[j] < a[j - 1]:
			right = j
			break
	minL = min(a[left:right + 1])
	maxR = max(a[left:right + 1])
	for i in range(left - 1, -1, -1):
		if a[i] < minL:
			left = i + 1
			break
	for j in range(right + 1, len(a)):
		if a[j] > maxR:
			right = j - 1
			break
	return (left, right)
# O(n)


a = [6,1,2,3,4,5,7,8,9]
print subSort(a)
print subSortBrute(a)