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

	def getNode(self, index):
		curr = self.head
		for _ in range(0,index):
			curr = curr.next
		return curr

	def append(self, node):
		curr = self.head
		while curr.next is not None:
			curr = curr.next
		curr.next = node

	def loopCheck(self):
		curr = self.head
		ids = set()
		while True:
			nodeId = id(curr)
			if nodeId in ids:
				break
			ids.add(nodeId)
			curr = curr.next
		return curr


l = LinkedList()
l.insert(1)
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(5)
l.insert(6)
l.insert(7)
node = l.getNode(4)
l.append(node)
loopingNode = l.loopCheck()
print loopingNode.data