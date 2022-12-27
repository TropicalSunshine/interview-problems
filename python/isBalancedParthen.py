#stack

L = "123{}[](())"
L1 = "(()"
## (()) true
## )()( false
## (() false

def inverse(i):
	if i == '}':
		return '{'
	elif i == ')':
		return '('
	elif i == ']':
		return '['

def isBalanced(s):
	stack = []

	for i in s:
		if i == '(' or i == '[' or i == '{':
			stack.append(i)
		elif i == ']' or i == '}' or i == ')':
			if(stack.pop() != inverse(i)):
				return False
	return (len(stack) == 0)
	
print(isBalanced(L))
print(isBalanced(L1)) 
