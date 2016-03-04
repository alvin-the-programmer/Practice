def flipTree(root):
	if root is None:
		return
	flipTree(root.left)
	flipTree(root.right)
	root.left, root.right = root.right, root.left
	