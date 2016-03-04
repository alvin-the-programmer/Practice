class Node: 
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BST:
	def __init__(self):
		self.root = None
	
	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
		else:
			self._insert(self.root, data)

	def _insert(self, root, data):
		if data < root.data:
			if root.left is not None:
				self._insert(root.left, data)
			else:
				root.left = Node(data)
		else:
			if root.right is not None:
				self._insert(root.right, data)
			else:
				root.right = Node(data)


	def printTree(self):
		self._printTree(self.root)

	def _printTree(self, root):
		if root is None:
			return
		else:
			self._printTree(root.left)
			print root.data
			self._printTree(root.right)
	
tree = BST()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(12)
tree.insert(100)
tree.insert(20)

