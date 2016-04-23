# O(n) runtime, O(1) space

def singleEdit(a, b):
	if singleSwap(a, b) or singleInsert(a, b):
		return True
	else:
		return False

def singleSwap(a, b):
	if len(a) != len(b):
		return False
	edit = 0
	for i in range(0, len(a)):
		if a[i] != b[i]:
			edit += 1
		if edit > 1:
			return False
	return True

def singleInsert(a, b):
	if len(a) == len(b):
		return False
	elif abs(len(a) - len(b)) > 1:
		return False
	if len(a) < len(b):
		a, b = b, a
	edit = 0
	for i in range(0, len(b)):
		if a[i] != b[i]:
			a = a[:i] + a[i + 1:]
			edit += 1
		if edit > 1:
			return False
	return True

print singleEdit('pale', 'ple')
print singleEdit('pales', 'pale')
print singleEdit('pale', 'bale')
print singleEdit('pale', 'pale')
print singleEdit('pale', 'bake')


