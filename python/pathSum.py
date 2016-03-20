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
	count = [0]
	sums = {}
	countPath(root, target, sums, count)
	return count[0]

def pathSum(root, target, sums, count):
	if root.data == target:
		count[0] += 1
	if root.left is None and root.right is None:
		sums[id(root)] = [root.data]
		return
	if id(root) not in sums:
		sums[id(root)] = [root.data]
	if root.left is not None:
		for s in sums[id(root.left)]:
			thisSum = root.data + s
			sums[id(root)].append(thisSum)
			if thisSum == target:
				count[0] += 1
	if root.right is not None:
		for s in sums[id(root.right)]:
			thisSum = root.data + s
			sums[id(root)].append(thisSum)
			if thisSum == target:
				count[0] += 1

def countPath(root, target, sums, count):
	if root is None:
		return
	countPath(root.left, target, sums, count)
	countPath(root.right, target, sums, count)
	pathSum(root, target, sums, count)



