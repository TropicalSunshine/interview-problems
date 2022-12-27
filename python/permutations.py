

def permutations_string(S):
    """
            abc
        abc     bac     cba
        acb
    """

    permutation_string_rec(list(S), 0)


permutations = {}
def permutation_string_rec(S, index):
    print(S)
    #current S is a permutation
    permutations["".join(S)] = True

    if len(S) == index:
        return
    else:
        for si in range(index, len(S)):
            #swap index position with si
            #then recurse
            NewS = S.copy()
            
            hold = NewS[index]
            NewS[index] = NewS[si]
            NewS[si] = hold

            permutation_string_rec(NewS, index + 1)

permutations_string("abc")

for i in permutations.keys():
    print(i)

