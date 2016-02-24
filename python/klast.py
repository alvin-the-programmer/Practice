def klast(k, root):
	ans = []
	_klast(k, root, ans)
	if ans:
		return ans[0]
	else:
		return None

def _klast(k, root, ans):
	if root.next is None:
		num = 1
	else:
		num = _klast(k, root.next, ans) + 1
	if num == k:
		ans.append(root)
	return num