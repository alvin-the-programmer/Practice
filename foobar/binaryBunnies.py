from random import shuffle
from time import time
from math import factorial

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


def countBuilds(root):
	if root is None:
		return 0
	return weave(countBuilds(root.left) * size(root.left), countBuilds(root.right) * size(root.right))

def size(root):
	if root is None:
		return 0
	return 1 + size(root.left) + size(root.right)

def weave(a, b):
	return factorial(a + b) / (factorial(b) * factorial(a))

def answer(seq):
	tree = Tree()
	tree.buildTree(seq[:])
	# print size(tree.root)
	print countBuilds(tree.root)

answer([10, 5, 6, 4, 15])
answer([10, 5, 15])
answer([10, 5,6, 15])
answer([5,9,8,2,1])



















