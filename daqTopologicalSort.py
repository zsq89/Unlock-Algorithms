import sys

def daqTopoSort(aDaq, root):
	orderList = []
	deg = getDaqDegree(aDaq)
	nextNode = []
	for key, value in deg.items():
		if deg[key] == 0: 
			nextNode.append(key)
	if root not in [""]:
		try:
			nextNode.remove(root)
		except ValueError as e:
			print(e)
			print("node \'" + root + "\' cannot be a root!")
			return orderList
		nextNode.insert(0, root)
	while len(nextNode) > 0:
		orderList.append(nextNode[0])
		for v in aDaq[nextNode[0]]:
			deg[v] -= 1
			if deg[v] == 0:
				nextNode.append(v)
		nextNode.pop(0)
	return orderList
	pass

def getDaqDegree(aDaq):
	degree = {}
	for key, value in aDaq.items():
		if key not in degree.keys():
			degree[key] = 0
		for v in value:
			if v in degree.keys():
				degree[v] += 1
			else:
				degree[v] = 1
	return degree

def main():
	daq = {
		'undershorts':['compression shorts'],
		'socks':['hose'],
		't-shirt':['chest pad'],
		'compression shorts':['hose','cup'],
		'hose':['pants'],
		'cup':['pants'],
		'chest pad':['sweater'],
		'pants':['skates','sweater'],
		'sweater':['mask'],
		'skates':['leg pads'],
		'mask':['catch glove'],
		'leg pads':['catch glove'],
		'catch glove':['blocker'],
		'blocker':[]
	}
	deg = getDaqDegree(daq)
	orderList = daqTopoSort(daq, "")
	for item in orderList:
		print(item)

if __name__ == '__main__':
    sys.exit(main())
