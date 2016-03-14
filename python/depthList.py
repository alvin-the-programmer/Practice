# working with tree class such as bst.py

class Lnode:
	def __init__(self, data):
		self.data = data
		self.next = None

def printList(head):
	if head is None:
		return
	print head.data
	printList(head.next)

def depthList(root):
	n = [root]
	l = []
	while n:
		l.append(Lnode(n[0].data))
		last = l[-1]
		for i in range(1, len(n)):
			last.next = Lnode(n[i].data)
			last = last.next
		m = len(n)
		for i in range(0, m):
			node = n.pop(0)
			if node.left is not None:
				n.append(node.left)
			if node.right is not None:
				n.append(node.right)
	for head in l:
		printList(head)
