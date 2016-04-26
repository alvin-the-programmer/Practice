def countSize(root):
	if root is None:
		return 0
	return countSize(root.left) + countSize(root.right) + 1

def countInRange(root, minVal, maxVal):
	if root is None:
		return 0
	if root.data >= minVal and root.data <= maxVal:
		thisNode = 1
	else:
		thisNode = 0
	return countInRange(root.left, minVal, maxVal) + countInRange(root.right, minVal, maxVal) + thisNode