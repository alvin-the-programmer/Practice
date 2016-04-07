def solution2(A):
	for i in range(0, len(A)):
		if sum(A[0:i]) == sum(A[i + 1: len(A)]):
			return i
	return -1

def solution(A):
	left = 0
	right = sum(A[1:len(A)])
	i = 0
	while i < len(A):
		if left == right:
			return i
		if i == len(A) - 1:
			break
		left = left + A[i]
		right = right - A[i + 1]
		i += 1
	return -1

a = [-5, 7, 3, -8]

print solution2(a)
print solution(a)
