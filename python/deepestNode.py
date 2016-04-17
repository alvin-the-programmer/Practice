class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

def findDeepest(root):
	deepest = [-1, None]
	traverse(root, 0, deepest)
	print 'node: ', deepest[1].data
	print 'depth:', deepest[0]
	return deepest

def traverse(root, depth, deepest):
	if root is None:
		return
	if depth > deepest[0]:
		deepest[0] = depth
		deepest[1] = root
	traverse(root.left, depth + 1, deepest)
	traverse(root.right, depth + 1, deepest)


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)

one.left = two
one.right = three
three.left = four
four.right = five
four.left = six
six.right = seven

findDeepest(one)