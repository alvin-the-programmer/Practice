class Node:
	def __init__(self, data, next):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = Node(None, None)
		self.size = 0

	def insert(self, data):
		curr = self.head
		while True:
			if curr.next is None:
				curr.next = Node(data, None)
				self.size += 1
				return
			elif curr.next.data > data:
				curr.next = Node(data, curr.next)
				self.size += 1
				return
			curr = curr.next

	def delete(self, data):
		prev = self.head
		curr = self.head.next
		while True:
			if curr.data == data:
				prev.next = curr.next
				self.size -= 1
				return
			elif curr.next is None:
				return
			prev = curr
			curr = curr.next

	def printSize(self):
		print "Size:",self.size

	def printAll(self):
		curr = self.head.next
		while True:
			if curr is None:
				print
				return
			print curr.data,
			curr = curr.next


def klast(k, root):
	ans = []
	_klast(k, root, ans)
	return ans[0]

def _klast(k, root, ans):
	if root.next is None:
		num = 1
	else:
		num = _klast(k, root.next, ans) + 1
	if num == k:
		ans.append(root)
	return num

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

print klast(9, l.head).data


