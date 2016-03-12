class Node():
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.parent = None

def inOrderSuccessor(node):
	if node.right is None:
		if node.parent.data > node.data:
			return node.parent.data
		elif node.parent.parent.data > node.data:
			return node.parent.parent.data
		else:
			return 'LAST NODE, NO SUCCESSOR'
	elif node.right is not None:
		curr = node.right
		while curr.left is not None:
			curr = curr.left
		return curr.data

ten = Node(10)
five = Node(5)
eight = Node(8)
eight.parent = five
five.right = eight
fifteen = Node(15)
twelve = Node(12)
eighteen = Node(18)
thirteen = Node(13)
thirteen.parent = twelve
twelve.right = thirteen
twelve.parent = fifteen
eighteen.parent = fifteen
fifteen.left = twelve
fifteen.right = eighteen
five.parent = ten
fifteen.parent = ten
ten.left = five
ten.right = fifteen

print inOrderSuccessor(twelve)