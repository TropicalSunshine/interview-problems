#https://leetcode.com/problems/group-anagrams/submissions/
from collections import defaultdict

def groupAnagrams( strs: [str]) -> [[str]]:
    anagrams = defaultdict(list)        
    for w in strs:
        sig = [0 for i in range(26)]
        for l in w:
            sig[ord(l) - ord('a')] += 1
        anagrams[tuple(sig)].append(w)

    result = []
    for k in anagrams.keys():
        result.append(anagrams[k])
    return result
        