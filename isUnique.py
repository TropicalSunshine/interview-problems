



def c(n : int):
    sum = 0
    while n != 0:
        digit = n % 10
        n /= 10
        n = int(n)
        sum += digit * digit
    return sum

"""
python 3 supports up to 18 digits and depending on the system
that means the largest digit someone can input is of size 18 and all 9's 
giving the largest calculation possible

18 * 81 = 1458
upper bound is at most 1458 cycles due to 
"""

def isUnque:
