def klast(k, root):
	ans = []
	_klast(k, root, ans)
	return ans[0]

def _klast(k, root, ans):
	if root.next is None:
		num = 1
	else:
		num = _klast(k, root.next, ans) + 1
	if num == k:
		ans.append(root)
	return num