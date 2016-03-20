# for tree, return (sum of values at odd levels) - (sum of values at even levels)

def evenOddDiff(root):
	s = [0]
	evenOdd(root, 0, s)
	return s[0]

def evenOdd(root, depth, s):
	if root is None:
		return
	if depth % 2 == 0:
		s[0] -= root.data
	else:
		s[0] += root.data
	evenOdd(root.left, depth + 1, s)
	evenOdd(root.right, depth + 1, s)