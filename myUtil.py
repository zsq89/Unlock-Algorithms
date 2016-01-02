'''
utilities for this package:
	print list vertically - printList
	print dictionary vertically - printDict
'''

def printList(aList):
	for item in aList:
		print(item)

def printDict(aDict):
	for key, value in aDict.items():
		print(str(key) + " : " + str(value))
