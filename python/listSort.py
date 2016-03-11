class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

def printL(head):
	if head is None:
		return
	else:
		print head.data
		printL(head.next)

def sortList(head):
	print 'sorting'
	l = []
	l.append(head)
	curr = head
	while curr.next is not None:
		curr = curr.next
		l.append(curr)
	sortedL = mergeSort(l)
	for i in range(0, len(sortedL) - 1):
		sortedL[i].next = sortedL[i + 1]
	sortedL[-1].next = None 

def mergeSort(l):
	if len(l) == 1:
		return l
	mid = len(l) / 2
	left = mergeSort(l[:mid])
	right = mergeSort(l[mid:])
	return merge(left, right)

def merge(a, b):
	result = []
	while a or b:
		if a and not b:
			result.append(a.pop(0))
		elif b and not a:
			result.append(b.pop(0))
		elif a[0].data < b[0].data:
			result.append(a.pop(0))
		else:
			result.append(b.pop(0))
	return result

fifty = Node(50)
fortyFive = Node(45)
seventyTwo = Node(72)
seventyFive = Node(75)
negativeTen = Node(-10)
negativeNine = Node(-9)
four = Node(4)
five = Node(5)

fifty.next = fortyFive
fortyFive.next = seventyTwo
seventyTwo.next = seventyFive
seventyFive.next = negativeTen
negativeTen.next = negativeNine
negativeNine.next = four
four.next = five;

printL(fifty)
sortList(fifty)
printL(negativeTen)


