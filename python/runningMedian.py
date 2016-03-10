from heapq import heappush
from heapq import heappop
from heapq import heappushpop

class median:
	def __init__(self):
		self.less = []
		self.more = []

	def add(self, n):
		if not self.less and not self.more:
			heappush(self.less, -n)
			return
		if n > -self.less[0]:
			heappush(self.more, n)
		else:
			heappush(self.less, -n)
		if (len(self.less) - len(self.more)) > 1:
			heappush(self.more, -heappop(self.less))
		elif (len(self.more) - len(self.less)) > 1:
			heappush(self.less, -heappop(self.more))


	def getMed(self):
		if len(self.less) == len(self.more):
			return (self.more[0] + -(self.less[0])) / 2.0
		elif len(self.less) > len(self.more):
			return -(self.less[0])
		elif len(self.more) > len(self.less):
			return self.more[0]

m = median()
m.add(10)
print m.getMed()
m.add(9)
print m.getMed()
m.add(11)
print m.getMed()
m.add(50)
print m.getMed()
m.add(7)
print m.getMed()
m.add(100)
print m.getMed()
m.add(101)
print m.getMed()

