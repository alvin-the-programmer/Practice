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

	def insertNode(self, node):
		nextNode = self.head
		self.head = node
		
	def delete(self, data):
		if self.head.data == data:
			self.head = self.head.next
		curr = self.head
		while curr is not None:
			if curr.data == data:
				prev.next = curr.next
				break
			prev = curr
			curr = curr.next

	def getHead(self):
		return self.head

	def printList(self):
		curr = self.head
		while curr is not None:
			print curr.data,
			curr = curr.next
		print

# return intersecting node
# or return false if no intersection
def getIntersection(list1, list2):
	a = list1.getHead()
	ids = set()
	while a is not None:
		ids.add(id(a))
		a = a.next
	b = list2.getHead()
	while b is not None:
		if id(b) in ids:
			return b
		b = b.next
	return false	


a = LinkedList()
a.insert(1)
a.insert(2)
a.insert(3)
a.insert(4)
a.insert(5)
print "list a:"
a.printList()
print "list b:"
b = LinkedList()
b.insertNode(a.getHead())
b.insert(6)
b.insert(7)
b.insert(8)
b.insert(9)
b.insert(10)
b.printList()
intersectNode = getIntersection(a,b)
print "intersection:"
print intersectNode.data
