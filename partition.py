class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def insert(self, data):
		nextNode = self.head
		self.head = Node(data, nextNode)

	def append(self, node):
		curr = self.head
		while curr.next is not None:
			curr = curr.next
		curr.next = node

	def printList(self):
		curr = self.head
		while curr is not None:
			print curr.data,
			curr = curr.next
		print
	def getHead(self):
		return self.head

def parition(head, item):
	less = LinkedList()
	more = LinkedList()
	curr = head
	while curr is not None:
		if curr.data < item:
			less.insert(curr.data)
		else:
			more.insert(curr.data)
		curr = curr.next
	more.insert(item)
	moreHead = more.getHead()
	less.append(moreHead)
	less.printList()


l = LinkedList()
l.insert(7)
l.insert(1)
l.insert(3)
l.insert(10)
l.insert(2)
l.insert(6)
l.insert(5)
l.insert(4)
l.insert(1)
l.insert(9)
l.printList()
parition(l.getHead(), 5)


