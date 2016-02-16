def palindrome(string):
	mid = len(string) / 2
	for i in range(0, mid):
		if string[i] != string[-(i + 1)]:
			return False
	return True

print palindrome("abcdef")
print palindrome("abdef")
print palindrome("lool")
print palindrome("locol")


