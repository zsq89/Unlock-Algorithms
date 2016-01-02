'''
This file contains several search algorithms:
	binary search - binarySearch
	recursive binary search - recursiveBinSearch
It is assumed that the input:aList is sorted
into nondecreasing order
'''
import sys

def binarySearch(aList, target):
	p = 0
	r = len(aList) - 1
	q = int(r/2)
	while p <= r:
		if aList[q] == target:
			return q
		elif aList[q] > target:
			r = q - 1
		else:
			p = q + 1
		q = int((p + r) / 2)
	return None

def recursiveBinSearch(aList, p, r, target):
	if p <= r:
		q = int((p + r) / 2)
		if aList[q] == target:
			return q
		elif aList[q] > target:
			return recursiveBinSearch(aList, p, q-1, target)
		else:
			return recursiveBinSearch(aList, q+1, r, target)
	else:
		return None

def main():
	aList = [1,2,3,4,6,9,12,21,56]
	res = binarySearch(aList, 12)
	print(res)
	res = recursiveBinSearch(aList, 0, len(aList)-1, 12)
	print(res)

if __name__ == "__main__":
	sys.exit(main())