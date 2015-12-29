import sys
import math
from myUtil import printList
from daqTopologicalSort import daqTopoSort

INFINITY = math.inf

def getShortestPath(aDaq, edgeWeight, sourceNode, destNode):
	path = []
	prev, shortest = daqShortestPath(aDaq, edgeWeight, sourceNode)
	curNode = destNode
	while True:
		if curNode == None:
			break
		path.append(curNode)
		curNode = prev[curNode]

	if path[-1] != sourceNode:
		print("path from " + sourceNode + " to " + destNode + " doesn't exist!")
		return None, INFINITY
	else:
		path.reverse()
		return path, shortest[destNode]

	pass


def daqShortestPath(aDaq, edgeWeight, sourceNode):
	# initiate
	shortest = {}
	prev = {}
	for key in aDaq.keys():
		shortest[key] = INFINITY
		prev[key] = None
	shortest[sourceNode] = 0

	#relax nodes, taken in the order of topological sort
	order = daqTopoSort(aDaq, sourceNode)
	for node in order[1:]:
		adjNode = getAdjacentNodes(aDaq, node)
		for aNode in adjNode:
			# relax node and aNode
			if shortest[aNode] + edgeWeight[(aNode, node)] < shortest[node]:
				prev[node] = aNode
				shortest[node] = shortest[aNode] + edgeWeight[(aNode, node)]
	return prev, shortest
	pass

def nodeRelax(node1, node2, edgeWeight):
	pass

def getAdjacentNodes(aDaq, aNode):
	adjNode = []
	for key, value in aDaq.items():
		if aNode in value:
			adjNode.append(key)
	return adjNode

def daqGetEdges(aDaq):
	edges = []
	for key, value in aDaq.items():
		for v in value:
			edges.append((key, v))
	printList(edges)
	return edges
	pass

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
	sourceNode = "undershorts"
	edges = daqGetEdges(daq)
	edgeWeight = {}
	w = 1
	for e in edges:
		edgeWeight[e] = w
		w += 1
	print(edgeWeight)
	# prev, shortest = daqShortestPath(daq, edgeWeight, sourceNode)
	# print(prev)
	# print(shortest)
	destNode = "catch glove"
	path, pathWeight = getShortestPath(daq, edgeWeight, sourceNode, destNode)
	printList(path)
	print(pathWeight)
	pass

if __name__ == '__main__':
	sys.exit(main())
