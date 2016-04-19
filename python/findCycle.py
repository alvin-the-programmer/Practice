# O(v+e) time, O(v) space

def findCycle(n, g, thisVisited, visited):
	if n in thisVisited:
		return True
	if n in visited:
		return
	newVisited = set(thisVisited)
	newVisited.add(n)
	for node in g[n]:
		if findCycle(node, g, newVisited, visited):
			return True
	visited.add(n)
	return False

def containsCycle(g):
	visited = set()
	for v in g:
		if findCycle(v, g, set(), visited):
			return True
	return False

g = {1:[2], 2:[3], 3:[4, 5], 4:[5, 6], 5:[], 6:[], 7:[7]}
print containsCycle(g)
