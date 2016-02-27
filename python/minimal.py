import math

class Node:
	def __init__(self):
		self.data = None
		self.left = None
		self.right = None

def minimal(a):
	root = Node()
	_minimal(a, root)
	printOrder(root)

def _minimal(a, root):
	mid = int(math.floor(len(a) / 2.0))
	root.data = a[mid]
	lefta = a[:mid]
	righta = a[mid + 1:]
	if lefta:
		root.left = Node()
		_minimal(lefta, root.left)
	if righta:
		root.right = Node()
		_minimal(righta, root.right)

def printOrder(root):
	if root is None:
		return
	printOrder(root.left)
	print root.data
	printOrder(root.right)

a = [1,2,3,4,5,6,7,8,9,10,11,12]
minimal(a)