# BRUTE FORCE SOLUTION O(N^2) TIME:
# def pathSum(root, n, target, count):
# 	if n == target:
# 		count[0] += 1
# 	if root.left is not None:
# 		pathSum(root.left, n + root.left.data, target, count)
# 	if root.right is not None:
# 		pathSum(root.right, n + root.right.data, target, count)

# def countPath(root, target, count):
# 	if root is None:
# 		return
# 	else:
# 		pathSum(root, root.data, target, count)
# 		countPath(root.left, target, count)
# 		countPath(root.right, target, count)

# def countPathSum(root, target):
# 	count = [0]
# 	countPath(root, target, count)
# 	return count[0]

def countPathSum(root, target):
	count = 0
	sums = {}
	countPath(root, target, sums)
	for l in sums.values():
		for s in l:
			if s == target:
				count += 1
	return count

def pathSum(root, target, sums):
	if root.left is None and root.right is None:
		sums[id(root)] = [0, root.data]
		return
	if id(root) not in sums:
		sums[id(root)] = [0]
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




