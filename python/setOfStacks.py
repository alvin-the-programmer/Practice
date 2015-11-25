class SetOfStacks:
	def __init__(self):
		self.stacks = []
		self.stacks.append([])

	def push(self, item):
		if len(self.stacks[-1]) < 3:
			self.stacks[-1].append(item)
		else:
			print "adding new stack"
			self.stacks.append([])
			self.stacks[-1].append(item)
	def pop(self):
		item = self.stacks[-1].pop()
		if len(self.stacks[-1]) == 0:
			print "removing stack"
			self.stacks.pop()
		return item


stacks = SetOfStacks()
stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.push(4)
stacks.push(5)
stacks.push(6)
stacks.push(7)
stacks.push(8)

print stacks.pop()
print stacks.pop()
print stacks.pop()
print stacks.pop()
print stacks.pop()
print stacks.pop()
print stacks.pop()

