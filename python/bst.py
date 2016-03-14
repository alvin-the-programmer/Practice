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
tree.insert(50)
tree.insert(25)
tree.insert(75)
tree.insert(15)
tree.insert(35)
tree.insert(65)
tree.insert(85)
tree.insert(100)
tree.insert(0)

# tree.printTree()

def pathSum(root, n, target, count):
	if n == target:
		count[0] += 1
	if root.left is not None:
		pathSum(root.left, n + root.left.data, target, count)
	if root.right is not None:
		pathSum(root.right, n + root.right.data, target, count)

def countPath(root, target, count):
	if root is None:
		return
	else:
		pathSum(root, root.data, target, count)
		countPath(root.left, target, count)
		countPath(root.right, target, count)

def countPathSum(root, target):
	count = [0]
	countPath(root, target, count)
	return count[0]

print countPathSum(tree.root, 75)








