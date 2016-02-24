def buildOrder(projects, dependencies):
	dep = {x:y for x, y in dependencies}
	done = [p for p in projects if p not in dep.keys()]
	while any(p for p in projects if p not in done and dep[p] in done):
		done.extend([p for p in projects if p not in done and dep[p] in done])
	if len(done) == len(projects):
		return done
	else:
		return -1

projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('d','a'),('b','f'),('d','b'),('a','f'),('c','d')]
print buildOrder(projects, dependencies)

