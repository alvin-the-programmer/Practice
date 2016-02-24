from itertools import product

def numIslands(g):
	visited = set()
	islands = 0
	for r in range(len(g)):
		for c in range(len(g[0])):
			if (r,c) not in visited and g[r][c]:
				visited.add((r,c))
				bfs(g, r, c, visited)
				islands += 1
	return islands

def dfs(g, r, c, visited):
	neighbors = getNeighbors(g, r, c)
	neighbors -= visited
	visited |= neighbors
	for row, col in neighbors:
		dfs(g, row, col, visited)

def bfs(g, r, c, visited):
	q = []
	q.append((r, c))
	while q:
		row, col = q.pop(0)
		neighbors = getNeighbors(g, row, col)
		neighbors -= visited
		visited |= neighbors
		q.extend(neighbors)

def getNeighbors(g, r, c):
	offsets = list(product([-1, 0, 1], repeat=2))
	return {(r + y, c + x) for (y, x) in offsets if isValid(g, r + y, c + x)}

def isValid(g, r, c):
	if r < 0 or c < 0:
		return False
	if r >= len(g) or c >= len(g[0]):
		return False
	if g[r][c]:
		return True
	else:
		return False

g = [[1,0,0,1],
	 [1,1,0,0],
	 [1,0,0,1],
	 [1,1,1,1]]

print numIslands(g)