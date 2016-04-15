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

# O(n) runtime, where n is the the number total dirs given as input (not paths)
# or O(nl) where l is the length max length of dir names
def countMakesFast(existing, new):
	dirs = {}
	count = 0
	for e in existing:
		addDir(dirs, e)
	for n in new:
		count += addDir(dirs, n)
	return count

def addDir(dirs, new):
	new = new.split('/')
	new = new[1:]
	count = 0
	for nDir in new:
		if nDir in dirs:
			dirs = dirs[nDir]
		else:
			dirs[nDir] = {}
			dirs = dirs[nDir]
			count += 1
	return count

e = {'/a'}
n = {'/a/b', '/a/c', '/b/b'}
print countMakesFast(e, n)
e = {}
n = {'/home/gcj/finals', '/home/gcj/quals'}
print countMakesFast(e, n)


