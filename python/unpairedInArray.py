def findUnpairedElement(a):
	unpaired = a[0]
	for item in a[1:]:
		unpaired ^= item
	return unpaired

l = [1,7,1,3,4,5,5,4,3]
print findUnpairedElement(l)