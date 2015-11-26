class SortStack:
	def __init__(self):
		self.s = []

	def push(self, item):
		temp = []
		if len(self.s) == 0:
			self.s.append(item)
			return
		else:
			while self.s[-1] < item:
				temp.append(self.s.pop());
				if len(self.s) == 0:
					break;
			self.s.append(item)
			while len(temp):
				self.s.append(temp.pop())

	def pop(self):
		item = self.s.pop()
		print "pop ", item


myStack = SortStack()
myStack.push(14)
myStack.push(17)
myStack.push(20)
myStack.push(15)
myStack.push(3)
myStack.push(2)
myStack.push(16)
myStack.push(17)
myStack.push(25)
myStack.push(19)
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.pop()





