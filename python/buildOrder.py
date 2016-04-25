def buildOrder(projects, deps):
	ins = {p:set() for p in projects}
	outs = {p:set() for p in projects}
	for d in deps:
		ins[d[0]].add(d[1])
		outs[d[1]].add(d[0])
	order = topSort(outs, ins)
	return order

# O(V + E) time complexity O(V) space
def topSort(outs, ins):
	order = []
	ready = [n for n in ins.keys() if not ins[n]]
	while ready:
		n = ready.pop()
		order.append(n)
		for m in outs[n]:
			ins[m] -= {n}
			if not ins[m]:
				ready.append(m)
	if len(order) == len(outs):
		return order
	else:
		return -1

p1 = ['a', 'b', 'c', 'd', 'e', 'f']
d1 = [('d','a'),('b','f'),('d','b'),('a','f'),('c','d')]
print buildOrder(p1, d1)

p2 = [1,2,3]
d2 = [(1,2), (2,3), (3,1)]
print buildOrder(p2, d2)