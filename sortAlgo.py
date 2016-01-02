'''
This file contains several sorting algorithms:
selectionSort
'''
import sys

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

def main():
	aList = [2,5,1,25,20,6,12,9]
	sortedList = selectionSort(aList)
	print(sortedList)
	sortedList = insertionSort(aList)
	print(sortedList)

if __name__ == "__main__":
	sys.exit(main())