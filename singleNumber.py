

#https://leetcode.com/problems/single-number/

def singleNumber(nums: [int]) -> int:
	"""
	a famous problem utilizing the xor operator in python ^

	xor is exclusive or
	1 xor 0 = 1
	0 xor 1 = 1
	0 xor 0 = 0
	1 xor 1 = 0

	the problem asks use to find the number that is not repeated twice in the array
	we can easily find this by xor all the value in the array
	by doing so we are cancelling out all similar numbers in the array

	example:
	bti representation
		0 = 0000
		1 = 0001
		3 = 0011

	lets say the given array is [3, 3, 1]
	we start with result = 0

	0000 ^ 0011 = 0011
	0011 ^ 0011 = 0000
	0000 ^ 0001 = 0001

	0001 = 1 which is the result

	"""
	result = 0
	for n in nums:
		result ^= n
	return n

assert singleNumber([3,3,1]) == 1

