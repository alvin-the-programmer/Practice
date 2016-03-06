def treeToList(root):
	nodes = []
	inOrderList(root, nodes)
	for i in range(0, len(nodes) - 1):
		nodes[i].right = nodes[i + 1]
		nodes[i + 1].left = nodes[i]

def inOrderList(root, a):
	if root is None:
		return
	inOrderList(root.left, a)
	a.append(root)
	inOrderList(root.right, a)

def printList(root):
	if root is None:
		return
	print root.data
	printList(root.right)