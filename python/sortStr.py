def merge(s1, s2, key):
	ans = []
	while s1 or s2:
		if s1 and not s2:
			ans.append(s1.pop(0))
		elif s2 and not s1:
			ans.append(s2.pop(0))
		elif s1 and s2:
			if key[s1[0]] < key[s2[0]]:
				ans.append(s1.pop(0))
			else:
				ans.append(s2.pop(0))
	return ans

def mergeSort(s, key):
	if len(s) == 1:
		return s
	mid = len(s) / 2
	left = mergeSort(s[:mid], key)
	right = mergeSort(s[mid:], key)
	return merge(left, right, key)


def sort(str1, str2):
	order = {l : i  for i, l in enumerate(str2)}
	for l in str1:
		if l not in order:
			order[l] = len(str2)
	ans = mergeSort(list(str1), order)
	return ''.join(ans)

print sort("hello", "loade")
print sort("terrible", "brelt")



