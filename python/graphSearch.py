class Node:
	def __init__(self, data, neighbors):
		self.visited = False
		self.data = data
		self.neighbors = neighbors

def bfs(root):
	queue = []
	root.visited = True
	queue.append(root)
	while queue:
		node = queue.pop(0)
		print node.data
		for n in node.neighbors:
			if not n.visited:
				n.visited = True
				queue.append(n)

def dfs(root):
	root.visited = True;
	print root.data
	for n in root.neighbors:
		if not n.visited:
			n.visited = True
			dfs(n)


eight = Node(8, [])
seven = Node(7, [eight])
six = Node(6, [seven])
five = Node(5, [eight, six])
two = Node(2, [five])
three = Node(3, [five])
four = Node(4, [six])
one = Node(1, [two, three, four])

# bfs(one)
dfs(one)