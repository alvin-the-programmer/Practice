def nextMax(arr):
	if len(arr) < 2:
		return "error"
	largest = float("-inf")
	nextLargest = float("-inf")
	for i in arr:
		if i > largest:
			nextLargest = largest
			largest = i
		elif i > nextLargest:
			nextLargest = i
	return nextLargest


a = [10,4,6]
print nextMax(a)