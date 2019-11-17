
from collections import defaultdict





'''
every combination from size 0 to N
N = size of the array
'''

test_array = ['a','b','c']
#space complexity O(N)
#time complexity O(2^N)

def combination(array):

    #counting number of occurrence
    counts = defaultdict(lambda: 0)
    for a in array:
        counts[a] += 1

    s = [''] * len(counts.keys()) 
    count = [0] * len(counts.keys())
    index = 0

    for k, v in counts.items():
        s[index] = k
        count[index] = v
        index += 1

    string_array = [None] * len(array)
    print("count: ", count)
    print("output: ", string_array)
    print("strings: ", s)


    combination_rec(s, count, 0, string_array, 0)


def combination_rec(s, count, pos, output, length):

    for i in range(length):
	    print(output[i], end = '')
    print()

    for i in range(pos, len(s)):
        if (count[i] == 0):
           continue

        output[length] = s[i]
        count[i] -= 1
        combination_rec(s, count, i, output, length + 1)
        count[i] += 1


combination(test_array)



def combinations_subarray(array, N):
	if len(array) <= N:
		print(array)

	else:
		print(array[:N])
		combinations(array[1:], N)
	

