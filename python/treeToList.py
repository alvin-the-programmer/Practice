# last should be a list containing a dummy node to begin list O(1) space

def inOrderList(root, last):
	if root is None:
		return
	inOrderList(root.left, last)
	last[0].right = root 
	root.left = last[0]
	last[0] = root
	inOrderList(root.right, last)

def printL(root):
	if root is None:
		return
	print root.data
	printL(root.right)