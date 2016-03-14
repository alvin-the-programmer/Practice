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
tree.insert(20)
tree.insert(30)
tree.insert(75)
tree.insert(70)
tree.insert(80)

# tree.printTree()

def countPathSum(root, target):
	count = 0
	sums = {}
	countPath(root, target, sums)
	for l in sums.values():
		print l
		for s in l:
			if s == target:
				count += 1
	return count

def pathSum(root, target, sums):
	if root.left is None and root.right is None:
		sums[id(root)] = [root.data]
		return
	if id(root) not in sums:
		sums[id(root)] = [root.data]
	if root.left is not None:
		sums[id(root)].extend([(root.data + s) for s in sums[id(root.left)]])
	if root.right is not None:
		sums[id(root)].extend([(root.data + s) for s in sums[id(root.right)]])

def countPath(root, target, sums):
	if root is None:
		return
	countPath(root.left, target, sums)
	countPath(root.right, target, sums)
	pathSum(root, target, sums)

print countPathSum(tree.root, 75)







