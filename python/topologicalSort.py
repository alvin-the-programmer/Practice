def topSort(outs, ins):
	order = []
	ready = [n for n in ins.keys() if not ins[n]]
	while ready:
		n = ready.pop()
		order.append(n)
		for m in outs[n]:
			ins[m] -= {n}
			if not ins[m]:
				ready.append(m)
	return order

outs = {
		1:{3},
		2:{3,7},
		3:{4,6},
		4:{5,6},
		6:{5},
		5:{7},
		7:{8},
		8:{}
}

ins = {
		1:{},
		2:{},
		3:{1,2},
		4:{3},
		6:{3,4},
		5:{4,6},
		7:{2,5},
		8:{7}
}

print topSort(outs, ins)