from itertools import product
from copy import deepcopy

def debruijn(k, n):
	if isinstance(k, int):
		chars = [str(i) for i in range(0, k)]
	elif isinstance(k, str):
		chars = [c for c in k]
		k = len(k)
	length = k ** n
	print length
	tups = list(product(chars, repeat=n))
	strs = set(''.join(e) for e in tups)
	remaining = deepcopy(strs)
	ans = [];
	db(strs, remaining, "", length, ans)
	return ans

def db(strs, remainingStrs, seq, length, ans):
	if len(seq) == length:
		if isDb(strs, seq):
			ans.append(seq)
		else:
			return
	for s in remainingStrs:
		if len(seq) == 0:
			newSeq = seq + s
			newStrs = deepcopy(remainingStrs)
			newStrs.remove(s)
			db(strs, newStrs, newSeq, length, ans)
		elif squish(seq, s):
			newSeq = seq + s[-1]
			newStrs = deepcopy(remainingStrs)
			newStrs.remove(s)
			db(strs, newStrs, newSeq, length, ans)

def squish(str1, str2):
	if len(str1) == 0:
		return True
	elif str1[len(str1) - len(str2) + 1:] == str2[:len(str2) - 1]:
		return True
	else:
		return False

def isDb(strs, seq):
	circleSeq = seq + seq
	for s in strs:
		if s not in circleSeq:
			return False
	return True

x = debruijn(2, 3)


	