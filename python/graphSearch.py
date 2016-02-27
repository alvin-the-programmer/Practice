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

one = Node(1,[])
two = Node(2,[])
three = Node(3,[])
four = Node(4,[])
five = Node(5,[])
six = Node(6,[])
seven = Node(7,[])
eight = Node(8,[])

one.neighbors = [two, three]
three.neighbors = [four, two]
two.neighbors = [six, one]
eight.neighbors = [seven, six]

def isPath(a, b):
	aq = [a]
	bq = [b]
	avisited = {a}
	bvisited = {b}
	while aq or bq:
		bfsStep(aq, avisited)
		bfsStep(bq, bvisited)
		if avisited.intersection(bvisited):
			return True
	return False

def bfsStep(q, visited):
	print 'step'
	size = len(q)
	for i in range(size):
		node = q.pop(0)
		for n in node.neighbors:
			if n not in visited:
				print n.data
				visited.add(n)
				q.append(n)

print isPath(one, eight)

