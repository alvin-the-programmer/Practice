def solution(X):
	xstr = str(X)
	indices = []
	for i in range(0, len(xstr) - 1):
		if xstr[i] == xstr[i + 1]:
			indices.append(i)
	nums = [int(xstr[:i] + xstr[i + 1:]) for i in indices]
	return max(nums)

print solution(2839339001112)
