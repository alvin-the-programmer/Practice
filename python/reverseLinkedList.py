# for linked list with dummy head
# l is list class

def reverse(l, last, root):
	if root is None:
		l.head.next = last
		return
	next  = root.next
	root.next = last
	reverse(l, root, next)

# call with reverse(l, None, l.head.next)