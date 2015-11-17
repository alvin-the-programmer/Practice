
class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None
		self.size = 0

	def insert(self, data):
		if self.size == 0:
			self.head = Node(data, None)
			self.size += 1
		else:
			nextNode = self.head
			self.head = Node(data, nextNode)
			self.size += 1

	def getItem(self, index):
		curr = self.head
		for i in range(0, index):
			curr = curr.next
		return curr.data

	def getSize(self):
		return self.size

	def printAll(self):
		curr = self.head
		while True:
			if curr is None:
				print
				return
			print curr.data,
			curr = curr.next

	def getHead(self):
		return self.head

def isPalindrome(linkedList):
	stack = []
	length = linkedList.getSize()
	stackSize = length / 2
	for i in range(0, stackSize):
		stack.append(linkedList.getItem(i))
	if length % 2 == 1:
		stackSize += 1
	for j in range(stackSize, length):
		s = stack.pop()
		if s != linkedList.getItem(j):
			return False
	return True


def getSize(head):
	curr = head
	size = 1
	while curr.next is not None:
		size += 1
		curr = curr.next
	return size

def isPalindrome2(head):
	curr = head
	stack = []
	length = getSize(head)
	stackSize = length / 2
	for i in range(0, stackSize):
		stack.append(curr.data)
		curr = curr.next
	if length % 2 == 1:
		curr = curr.next
	while curr is not None:
		s = stack.pop()
		if s != curr.data:
			return False
		curr = curr.next
	return True


l = LinkedList()
l.insert(4)
l.insert(3)
l.insert(2)
l.insert(1)
l.insert(100)
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.printAll()
head = l.getHead()
print "length = ", getSize(head)
print "isPalindrome = ", isPalindrome2(head)