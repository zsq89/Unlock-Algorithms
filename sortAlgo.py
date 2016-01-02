'''
This file contains several sorting algorithms:
selectionSort
'''
import sys
from math import inf

INFINITY = inf

def selectionSort(aList):
	for i in range(0, len(aList)-1):
		minInd = i
		for j in range(i+1, len(aList)):
			if aList[j] < aList[minInd]:
				minInd = j
		temp = aList[i]
		aList[i] = aList[minInd]
		aList[minInd] = temp
	return aList

def insertionSort(aList):
	for i in range(1, len(aList)):
		keyNum = aList[i]
		j = i - 1
		while j >= 0 and aList[j] > keyNum:
			aList[j+1] = aList[j]
			j -= 1
		aList[j+1] = keyNum
	return aList

def mergeSort(aList, p, r):
	if p >= r:
		return
	else:
		q = int((p + r) / 2)
		mergeSort(aList, p, q)
		mergeSort(aList, q+1, r)
		mergeList(aList, p, q, r)

def mergeList(aList, p, q, r):
	lList = aList[p:q+1]
	lList.append(INFINITY)
	rList = aList[q+1:r+1]
	rList.append(INFINITY)
	i = 0
	j = 0
	for k in range(p, r+1):
		if lList[i] <= rList[j]:
			aList[k] = lList[i]
			i += 1
		else:
			aList[k] = rList[j]
			j += 1

def quickSort(aList, p, r):
	if p >=r:
		return
	else:
		q = partitionList(aList, p, r)
		quickSort(aList, p, q-1)
		quickSort(aList, q+1, r)

def partitionList(aList, p, r):
	# Choose aList[r] as the pivot
	# k is used to trace the leftmost index of right partition
	k = p
	for i in range(p, r):
		if aList[i] < aList[r]:
			# if aList[i] comes before the pivot,
			# swap it with the leftmost of right partition, i.e. aList[k]
			# since left partition increases by 1, shift k to the right by 1
			temp = aList[k]
			aList[k] = aList[i]
			aList[i] = temp
			k += 1
	# after partition, swap the pivot with the element at k
	# return the index of pivot
	temp = aList[k]
	aList[k] = aList[r]
	aList[r] = temp
	return k
	
def main():
	aList = [2,5,1,25,20,6,12,9]
	sortedList = selectionSort(aList)
	print(sortedList)
	sortedList = insertionSort(aList)
	print(sortedList)
	mergeSort(aList, 0, len(aList)-1)
	print(aList)
	aList1 = aList
	quickSort(aList1, 0, len(aList1)-1)
	print(aList1)

if __name__ == "__main__":
	sys.exit(main())