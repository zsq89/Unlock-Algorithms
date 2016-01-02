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
	mid = int(r/2)
	while p <= r:
		if aList[mid] == target:
			return mid
		elif aList[mid] > target:
			r = mid - 1
		else:
			p = mid + 1
		mid = int((p + r) / 2)
	return None

def recursiveBinSearch(aList, p, r, target):
	if p <= r:
		mid = int((p + r) / 2)
		if aList[mid] == target:
			return mid
		elif aList[mid] > target:
			return recursiveBinSearch(aList, p, mid-1, target)
		else:
			return recursiveBinSearch(aList, mid+1, r, target)
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