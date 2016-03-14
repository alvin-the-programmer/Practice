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
