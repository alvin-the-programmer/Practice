class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = Node(None, None)

	def insert(self, data):
		curr = self.head
		while True:
			if curr.next is None:
				curr.next = Node(data, None)
				return
			elif curr.next.data > data:
				curr.next = Node(data, curr.next)
				return
			curr = curr.next
		return

	def delete(self, data):
		prev = self.head
		curr = self.head.next
		while True:
			if curr.data == data:
				prev.next = curr.next
				return
			elif curr.next is None:
				return
			prev = curr
			curr = curr.next

	def printAll(self):
		curr = self.head.next
		while True:
			if curr is None:
				return
			print curr.data
			curr = curr.next
		return

l = LinkedList()
l.insert(30)
l.insert(32)
l.insert(0)
l.insert(30)
l.insert(29)
l.insert(15)
l.insert(22)
l.insert(-2)
l.insert(-2)
l.insert(0)
l.insert(-1)
l.insert(102)
l.delete(0)
l.delete(102)
l.delete(-2)
l.printAll()


