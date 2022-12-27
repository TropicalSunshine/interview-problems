
#https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem

alph = "abcdefghijklmnopqrstuvwxyz"

def sherlockAndAnagrams():
	sigs = {}
	sig = [0 for i in range(len(alph))]

	for c in s:
		sig[ord(c) - ord('a')] += 1
	
	for start in range(len(s)):
		for finish in range(start, len(s)):
			sig = [0 for i in range(len(alph))]
			for c in s[start:finish + 1]:
				sig[ord(c) - ord('a')] += 1

			if tuple(sig) in sigs:
				sigs[tuple] += 1
			else:
				sigs[tuple(sig)] = 1
	count = 0

	for key in sigs:
		n = sigs[key]
		count += (n * (n - 1)) / 2
	return int(count)

