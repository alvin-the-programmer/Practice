
def subsetPrint(l):
	myList = []
	for (ele, val) in l:
		if val == True:
			myList.append(ele)
	print myList

def getSubsets(l, index):
	if len(l) == index:
		subsetPrint(l)
	else:	
		e = l[index]
		eTrue = (e, True)
		eFalse = (e, False)
		list1 = l[:]
		list2 = l[:]
		list1[index] = eTrue
		list2[index] = eFalse
		getSubsets(list1, index + 1)
		getSubsets(list2, index + 1)


myList = [1,2,3,4,5]
list2 = ['a','b','c']
getSubsets(list2, 0)