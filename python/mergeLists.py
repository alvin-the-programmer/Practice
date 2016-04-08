def mergeLists(lists):
	result = []
	for l in lists:
		result = merge(l, result)
	return result

def merge(alist, blist):
	ans = []
	a = alist[:]
	b = blist[:]
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

a = [1,2,3,4,5,6,7,8,9,10]
b = [2,4,6,8,10]
c = [5,10,15]
d = [3]
e = [7,21,28]
f = [9,9,9]
lists = [a,b,c,d,e,f]
print mergeLists(lists)


