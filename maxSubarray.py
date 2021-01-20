import sys



def naive(arr : [int]) -> int:
	"""
	O(N^2)  ~O(N^3) - inner loop
	the naive method is to list all possible subarrays
	find the largest subarray
	"""
	result = -sys.maxsize
	
	for start in range(len(arr)):
		for finish in range(start, len(arr)):
			s = 0
			for v in arr[start:finish + 1]:
				s += v
			result = max(s, result)
	return result

#test case from leetcode
assert naive([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def maxSubarray(arr: [int]) -> int:
	"""
	at every position of the arr we consider this:
		1) is the sum we have accumulated so far greater than sum + current value
		2) is the the current value greater than the previous sum

		thus we are trying to find max(arr[i], s + arr[i]) at every position

		a variable to keep track of the largest value found is also necessary

		known as Kadene's method
	"""
	result = -sys.maxsize
	s = 0

	for i in range(len(arr)):
		s = max(s + arr[i], arr[i])
		result = max(s, result)
	
	return result

#test case from leetcode
assert maxSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
