from collections import Counter

class Node:
	def __init__(self):
		self.data = None
		self.left = None
		self.right = None

def splitSeq(s, k):
	kcount = Counter(k)
	for i in range(len(k), len(s) + 1):
		if Counter(s[:i]) == kcount:
			return s[:i], s[i:]

def buildTree(inorder, preorder, node):
	node.data = preorder[0]
	i = inorder.index(preorder[0])
	lInorder = inorder[:i]
	rInorder = inorder[i+1:]
	lPreorder, rPreorder = splitSeq(preorder[1:], lInorder)
	if lInorder:
		node.left = Node()
		buildTree(lInorder, lPreorder, node.left)
	if rInorder:
		node.right = Node()
		buildTree(rInorder, rPreorder, node.right)

def printTree(root):
	if root is None:
		return
	else:
		printTree(root.left)
		print root.data
		printTree(root.right)

print "balanced tree: "
inorder = [3, 5, 7 , 10, 13, 15, 17]
preorder = [10, 5 , 3, 7, 15, 13, 17]
root = Node()
buildTree(inorder, preorder, root)
printTree(root)

print "unbalanced tree input: "
inorder = [5, 10, 13, 15, 16, 17]
preorder = [10, 5, 15, 13, 17, 16]
root = Node()
buildTree(inorder, preorder, root)
printTree(root)