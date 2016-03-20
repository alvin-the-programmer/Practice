from random import shuffle
from time import time

class Node():
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class Tree():
	def __init__(self):
		self.root = None
		self.childMap = {}

	def insert(self, node, n):
		if n not in self.childMap.keys():
			self.childMap[n] = set()
		if self.root is None:
			self.root = Node(n)
			return
		if n < node.data:
			if node.right is None:
				node.right = Node(n)
				self.childMap[node.data].add(n)
			else:
				self.insert(node.right, n)
		elif n > node.data:
			if node.left is None:
				node.left = Node(n)
				self.childMap[node.data].add(n)
			else:
				self.insert(node.left, n)

	def buildTree(self, l):
		while l:
			self.insert(self.root, l.pop(0))

	def printTree(self, node):
		if node is None:
			return
		else:
			self.printTree(node.left)
			print node.data
			self.printTree(node.right)

def permute(l, frontier, numChildren, childMap, count):
	if len(l) == len(childMap):
		count[0] += 1
		return
	newFrontier = set()
	for parent in frontier:
		if numChildren[parent] < 2:
			newFrontier.add(parent)
	for parent in newFrontier:
		for c in childMap[parent]:
			if c not in l:
				thisL = l.copy()
				thisL.add(c)
				thisFrontier = newFrontier.copy()
				thisFrontier.add(c)
				thisNumChildren = numChildren.copy()
				thisNumChildren[parent] += 1
				permute(thisL, thisFrontier, thisNumChildren, childMap, count)

def answer(seq):
	tree = Tree()
	tree.buildTree(seq[:])
	count = [0]
	numChildren = {i: 0 for i in seq}
	permute({seq[0]}, {seq[0]}, numChildren, tree.childMap, count)
	return str(count[0])

print answer([5, 9, 8, 2, 1])
print answer([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

l = [i for i in range(1, 17)]
shuffle(l)
start = time()
ans = answer(l)
end = time()
print "time: ", end - start
print ans

