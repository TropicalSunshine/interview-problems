

def subsets(array):
    if array == []:
        return
    else:
        print(array)
    
        
        #take one index off of each edge and pass to recursive
        #call
        subsets(array[:-1])
        subsets(array[1:])


subsets([1,2,3,4,5])


