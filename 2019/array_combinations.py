
from collections import defaultdict

def combination(array):
    counts = defaultdict(lambda: 0)

    for a in array:
        counts[a] += 1

    s = [] 
    count = []
    index = 0

    for k, v in counts.items():
        s[index] = k
        count[index] = v
        index += 1

    string_array = [''] * len(array)
    combination_rec(s, count, 0, string_array, 0)


def combination_rec(s, count, pos, output, length):
        print(output, length)
        for i in range(pos, len(s)):
            if (count[i] == 0):
                continue

            output[length] = s[i]
            count[i] -= 1
            combination_rec(s, count, i, output, length + 1)
            count[i] += 1


combination([1,2,3,4])

