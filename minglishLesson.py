def answer(words):
    graph = makeGraph(words)
    start = getStartNodes(graph)
    sort = []
    visited = []

    def visit(node):
        if node not in visited:
            visited.append(node)
            if node in graph:
                for neighbor in graph[node]:
                    visit(neighbor)
            sort.append(node)

    for node in start:
        visit(node)
    ans = ''.join(sort[::-1])
    return ans

def getEdge(a, b):
	length = min(len(a), len(b))
	for i in range(length):
		if a[i] != b[i]:
			return a[i], b[i]

def getStartNodes(graph):
    e = set()
    for edges in graph.values():
        e.update(edges)
    sNodes = set(n for n in graph if n not in e)
    return sNodes

def makeGraph(words):
	graph = {}
	for i in range(len(words) - 1):
		edge = getEdge(words[i], words[i + 1])
		if edge is not None:
			if edge[0] in graph:
				graph[edge[0]].append(edge[1])
			else:
				graph[edge[0]] = [edge[1]]
	return graph




print answer(["ba", "ab", "cb"])