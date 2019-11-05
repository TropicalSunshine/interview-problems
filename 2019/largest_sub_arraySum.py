




L = [-2, -3, 4, -1, -2, 1, 5, -3]

##brute force solution
def sumArrayBruteForce(L):
	if len(L) == 1:
		return L[0]
	else:
		s = sum(L)
		s1 = sumArrayBruteForce(L[1:])
		s2 = sumArrayBruteForce(L[:-1])
		
		m = max(s, s1)
		m = max(m, s2)

		return m
		


##optimized solution
def sumArray(L):
	
	sCheck = L[0]
	s = L[0]

	for i in range(1, len(L)):
		sCheck += L[i]
		
		if sCheck > s:
			s = sCheck
				
		if L[i] > s:
			s = L[i]
			sCheck = L[i]
	return s  

print(sumArrayBruteForce(L))
print(sumArray(L))


