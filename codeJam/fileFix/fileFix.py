# O(n^2 * l) runtime, where l is the length of the longest path

def countMakes(existing, new):
	if not existing:
		existing = {''}
	existing = {path + '/' for path in existing}
	new = {path + '/' for path in new}
	count = 0
	for newDir in new:
		diffs = [matchDir(newDir, newDir) - matchDir(newDir, d) for d in existing]
		count += min(diffs)
		existing.add(newDir)
	return count

def matchDir(a, b):
	if len(a) < len(b):
		length = len(a)
	else:
		length = len(b)
	count = 0
	for i in range(1, length):
		if a[i] != b[i]:
			break
		if a[i] == '/':
			count += 1
	return count

e = {'/a'}
n = {'/a/b', '/a/c', '/b/b'}
print countMakes(e, n)

e = {}
n = {'/home/gcj/finals', '/home/gcj/quals'}
print countMakes(e, n)