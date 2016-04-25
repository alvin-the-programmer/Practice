class Iterator:
	def __init__(self, iterable):
		self.iterable = iterable
		self.i = 0

	def next(self):
		if self.i >= len(self.iterable):
			raise StopIteration
		item = self.iterable[self.i]
		self.i += 1
		return item

l = [0,2,4,6,8,10]
it = Iterator(l)

# will raise exception
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()
print it.next()