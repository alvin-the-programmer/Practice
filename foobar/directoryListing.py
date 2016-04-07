def solution(S):
	a = S.splitlines()
	images = []
	for i in range(0, len(a)):
		if not "." in a[i]:
			lvl = len(a[i]) - len(a[i].lstrip(' '))
			for j in range(i + 1, len(a)):
				if lvl >= (len(a[j]) - len(a[j].lstrip(' '))):
					i = j
					break
				if lvl == (len(a[j]) - len(a[j].lstrip(' ')) - 1):
					if (".jpeg" in a[j]) or (".png" in a[j]) or (".gif" in a[j]):
						images.append(i)
	total = 0
	for i in range(0, len(a)):
		if (".jpeg" in a[i]) or (".png" in a[i]) or (".gif" in a[i]):
			if len(a[i]) == len(a[i].lstrip(' ')):
				total += 1
				break
	for k in images:
		total += findPathLen(a, k)
	return total

def findPathLen(a, k):
	lastlvl = len(a[k]) - len(a[k].lstrip(' '))
	path = '/' + a[k]
	for i in range(k - 1, -1, -1):
		if not "." in a[i]:
			if lastlvl - 1 == (len(a[i]) - len(a[i].lstrip(' '))):
				path += '/' + a[i]
	return len(path.replace(' ', ''))

s = """dir1
me.jpeg
you.gif
 dir11
 dir12
  picture.jpeg
  dir121
  file1.txt
dir2
 file2.gif"""

print solution(s)