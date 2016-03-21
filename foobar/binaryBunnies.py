from math import factorial

class Node():
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class Tree():
	def __init__(self):
		self.root = None

	def insert(self, node, n):
		if self.root is None:
			self.root = Node(n)
			return
		if n < node.data:
			if node.right is None:
				node.right = Node(n)
			else:
				self.insert(node.right, n)
		elif n > node.data:
			if node.left is None:
				node.left = Node(n)
			else:
				self.insert(node.left, n)

	def buildTree(self, l):
		while l:
			self.insert(self.root, l.pop(0))

def countBuilds(root):
	if root is None:
		return 1
	return weave(size(root.left), size(root.right)) * countBuilds(root.left) * countBuilds(root.right)

def size(root):
	if root is None:
		return 0
	return 1 + size(root.left) + size(root.right)

def weave(a, b):
	return factorial(a + b) / (factorial(b) * factorial(a))

def answer(seq):
	tree = Tree()
	tree.buildTree(seq[:])
	return str(countBuilds(tree.root))